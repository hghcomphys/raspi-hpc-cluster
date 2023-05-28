import os
import batchspawner
import sys
c = get_config()

# Select the Torque backend and increase the timeout since batch jobs may take time to start
c.JupyterHub.spawner_class = 'wrapspawner.ProfilesSpawner'
# c.JupyterHub.spawner_class = 'batchspawner.SlurmSpawner'
c.Spawner.http_timeout = 30

c.JupyterHub.hub_ip = "rplogin01"
c.JupyterHub.ip = '192.168.0.100'
#c.jupyterhub.port = 443

c.Spawner.default_url = "/lab"

c.SlurmSpawner.batch_script = '''#!/bin/bash -i
#SBATCH --chdir=/home/{username}
#SBATCH --time={runtime}
#SBATCH --output={homedir}/.jupyterhub_slurmspawner.log
#SBATCH --partition={partition}
#SBATCH --job-name=jupyter
#SBATCH --cpus-per-task={nprocs}
#SBATCH --mem={memory}
##SBATCH --gres={ngpus}
#export PATH=/nfs/miniforge3/envs/jupyterhub/bin:$PATH
{cmd}
'''

#-------------------------------
# ProfilesSpawner configuration 
#-------------------------------
# List of profiles to offer for 
#   List(Tuple( Unicode, Unicode
# corresponding to profile displ
# dictionary of spawner config o
#                               
# The first three values will be
# {key}, and {type}             
#                               
c.ProfilesSpawner.profiles = [
     ('Host process', 'local', 'jupyterhub.spawner.LocalProcessSpawner', {'ip':'0.0.0.0'}),
     ('SLURM 1 cores, 200 MB', 'slurm1c200mb1d', 'batchspawner.SlurmSpawner', dict(req_partition='jupyter', req_nprocs='1', req_runtime='1-00:00:00', req_memory='200M')),
     ('SLURM 2 cores, 500  MB', 'slurm2c500mb1d', 'batchspawner.SlurmSpawner', dict(req_partition='jupyter', req_nprocs='2', req_runtime='1-00:00:00', req_memory='500M')),
     ('SLURM 4 cores, 1000 MB', 'slurm4c1000mb1d', 'batchspawner.SlurmSpawner', dict(req_partition='jupyter', req_nprocs='4', req_runtime='1-00:00:00', req_memory='1000M')),
     ]

#c.JupyterHub.services = [
#    {
#        "name": "jupyterhub-idle-culler-service",
#        "command": [
#            '/usr/bin/python3',
#            "-m", "jupyterhub_idle_culler",
#            "--timeout=30",
#        ],
#        # "admin": True,
#    }
#]

