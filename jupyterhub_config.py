import os

import batchspawner

c = get_config()

# Select the Torque backend and increase the timeout since batch jobs may take time to start
c.JupyterHub.spawner_class = "wrapspawner.ProfilesSpawner"
# c.JupyterHub.spawner_class = 'batchspawner.SlurmSpawner'
c.Spawner.http_timeout = 30

c.JupyterHub.hub_ip = "rplogin01"
c.JupyterHub.ip = "192.168.0.100"
# c.jupyterhub.port = 443

c.Spawner.default_url = "/lab"

c.SlurmSpawner.batch_script = """#!/bin/bash -i
#SBATCH --chdir=/home/{username}
#SBATCH --time={runtime}
#SBATCH --output={homedir}/.jupyterhub_slurmspawner.log
#SBATCH --job-name=jupyter
#SBATCH --cpus-per-task={nprocs}
#SBATCH --mem={memory}
##SBATCH --gres={ngpus}
#export PATH=/nfs/miniforge3/envs/jupyterhub/bin:$PATH
{cmd}
"""

# -------------------------------
# ProfilesSpawner configuration
# -------------------------------
# List of profiles to offer for
#   List(Tuple( Unicode, Unicode
# corresponding to profile displ
# dictionary of spawner config o
#
# The first three values will be
# {key}, and {type}
#
c.ProfilesSpawner.profiles = [
    (
        "Host process",
        "local",
        "jupyterhub.spawner.LocalProcessSpawner",
        {"ip": "0.0.0.0"},
    ),
    (
        "SLURM 2 cores, 500  MB",
        "slurm2c500mb1d",
        "batchspawner.SlurmSpawner",
        dict(
            req_partition="debug",
            req_nprocs="2",
            req_runtime="1-00:00:00",
            req_memory="500M",
        ),
    ),
    (
        "SLURM 4 cores, 1000 MB",
        "slurm4c1000mb1d",
        "batchspawner.SlurmSpawner",
        dict(
            req_partition="debug",
            req_nprocs="4",
            req_runtime="1-00:00:00",
            req_memory="1000M",
        ),
    ),
]

# shutdown idle notebooks
c.JupyterHub.services = [
    {
        "name": "cull-idle",
        "admin": True,
        "command": [
            os.sys.executable,
            "/srv/jupyterhub/cull_idle_servers.py",
            "--timeout=3600",
        ],
    }
]
