# Raspberry Pi Cluster

## Currently:
- [SLURM](https://github.com/SchedMD/slurm) version `20.02` workload manager was built from source code and was succesfully tested on `Raspberry Pi 4 Model B 2GB` on `Raspbian 64 bit`. 

## Installation:
Instructions are pretty much as are stated in `https://github.com/mknoxnv/ubuntu-slurm` except minor changes are required as follows:
- some prerequisite packages are different on `raspbian` (e.g. libmariadbclient)
- `aarch64` architecture instead of `x86_64` (--enable-pam --with-pam_dir=/lib/aarch64-linux-gnu/security/
- `slurm.conf`
- `slurmdbd.conf`
- enable cgroup memory (`/boot/cmdline.txt`)

## Multi-node:
- set `master` and `worker` hostnames in `/etc/hosts`
- copy the `munge.key` of `master` node into the 'workder' nodes 
- enable and start `slurmd` on `worker` nodes
- same `slurm.conf` between all nodes

Check nodes:
```
sinfo
srun -n5 hostname
```
Update the states of a node:
```
scontrol update nodename=node02 state=idle
```