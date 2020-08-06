# Raspberry Pi Cluster

## Currently:
- [SLURM](https://github.com/SchedMD/slurm) version `20.02` workload manager was built from source code and was successfully tested on `Raspberry Pi 4 Model B 2GB` on `Raspbian 64 bit`. 

## Installation:
Instructions are pretty much as are stated in `https://github.com/mknoxnv/ubuntu-slurm` except minor changes are required as follows:
- some prerequisite packages are different on `raspbian` (e.g. libmariadbclient)
- `aarch64` architecture instead of `x86_64` (--enable-pam --with-pam_dir=/lib/aarch64-linux-gnu/security/
- `slurm.conf`
- `slurmdbd.conf`
- enable cgroup memory (`/boot/cmdline.txt`)

## Multi-node:
- set `master` and `worker` hostnames in `/etc/hosts`
- copy the `munge.key` of `master` node into the 'worker' nodes 
- enable and start `slurmd` on `worker` nodes
- same `slurm.conf` between all nodes
- NFS from the master to all worker nodes

Check nodes:
```
sinfo
srun --nodes=2 hostname
```
Update the states of a node:
```
scontrol update nodename=node02 state=idle
```

## Network File Share (NFS):
`/home` and `/storage` have to be mounted from the master. If automatic mounting in `fastb` doesn't work try:
```
sudo raspi-config
```
and selecting Wait for the network at boot/Yes.

Module and packages can be built on master nodes and shared through NFS to other worker nodes, such as `/nfs/apps`. So, other compute nodes execute them without the need to install them on each node separately.

## Login node:
`Login node` is required in order to limit, or even block, users access to master and worker nodes for security reasons. On the other side, users have to be able to test their codes and submit their jobs from the login node(s). 

Logging node is in fact a `worker node` that is not used in any of `partitions`. This allows users to remotely connect, through ssh, and submit jobs.

It can be configured by simply removing the login node's hostname from partition nodes of the `slurm.conf` file. 

## Setup Jupyterhub:
Conda or Miniconda, at this moment, does not support jupyterhub installation on raspberry pi. Therefore, it requires to directly install it from `apt-get python3-pip` and `pip3` commands.

How to install jupyterhub on `raspbian 64bit`:
```
sudo apt-get update 
sudo apt-get install python3-pip 
sudo -H pip3 install --upgrade pip

sudo apt-get install npm 
sudo npm install -g configurable-http-proxy

sudo install libffi-dev
sudo -H pip3 install notebook jupyterhub
```

`master` node: jupyterhub and its config file (see `jupyterhub_config.py`) has to be setup file. Also `batchspawner` and `wrapspawner` for its integration with Slurm has to install from their git repos. 

Master node is the place where jupyterhub service runs and then users access the service through the preset jupyterhub `ip` and `port` in the config file.

`worker` node: only `notebook` and `batchspawner` are required. If it does not work, install `jupyterhub` and `wrapspawner` packages as well.
