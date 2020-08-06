import os
import batchspawner
c = get_config()

# Select the Torque backend and increase the timeout since batch jobs may take time to start
c.JupyterHub.spawner_class = 'wrapspawner.ProfilesSpawner'
# c.JupyterHub.spawner_class = 'batchspawner.SlurmSpawner'
c.Spawner.http_timeout = 30

c.BatchSpawnerBase.req_host = 'node01'
c.BatchSpawnerBase.req_runtime = '12:00:00'

c.JupyterHub.hub_ip = "node01"
c.JupyterHub.ip = '192.168.0.10'
c.jupyterhub.port = 443

c.SlurmSpawner.batch_script = '''
#SBATCH --chdir=/home/{username}
#SBATCH --partition='{partition}
#SBATCH --time={runtime}        
#SBATCH --output={homedir}/jupyt
#SBATCH --job-name=jupyterhub-sp
#SBATCH --cpus-per-task={nprocs}
#SBATCH --mem={memory}          
##SBATCH --gres={ngpus}         
#sh /home/hossein/anaconda3/etc/
#conda activate jupyterhub      
#export PATH=/home/hossein/anaco
#source /env/python2020/bin/acti
#source /opt/jupyterhub/minicond
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
     ('1) SLURM 2 cores, 750  MB', 'slurm1c250mb2d', 'batchspawner.SlurmSpawner', dict(req_partition='debug', req_nprocs='1', req_runtime='2-00:00:00', req_memory='750M')),
     ('2) SLURM 4 cores, 1500 MB', 'slurm2c500mb2d', 'batchspawner.SlurmSpawner', dict(req_partition='debug', req_nprocs='4', req_runtime='2-00:00:00', req_memory='1500M'))
]

# shutdown idle notbooks
#c.JupyterHub.services = [
#    {
#        'name': 'cull-idle',
#        'admin': True,
#        'command': [os.sys.executable, '/opt/jupyterhub/cull_idle_servers.py', '--timeout=3600'],
#    }
#]

 