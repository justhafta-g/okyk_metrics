Project for GL

# Description:

Script prints basic information about OS to console. 

## The script accept a single parameter to specify which metrics set to print:

```
cpu - prints CPU metrics
mem - prints RAM metrics
```
### Requirements:
```
python3
pip3
psutil
```
## Installation:

git clone https://github.com/wbdevops/okyk_metrics.git
sudo apt install python3-pip

## CPU Metrics:
### Sample output:
``
python sys_mertrics.py cpu
`` 
  system.cpu.idle 78.8
  system.cpu.user 17.3
  system.cpu.guest 0.0
  system.cpu.iowait 1.3
  system.cpu.stolen 0.0
  system.cpu.system 2.5

## Memory Metrics:
### Sample output:
``
python sys_metrics.py mem
```
 virtual total 16712351744
 virtual used 9190146048
 virtual free 1391624192
 virtual shared 287655116
 swap total 0
 swap used 0
 swap free 0

## Docker:

Script could be run from the docker container. Docker should be installed.

##  Docker Hub:

ht<span>tps://</span>hub.docker.com/r/okyktenko/sys_metrics  

##  Before run:

docker pull okyktenko/sys_metrics:latest

## Run:

### Memory metrics:

docker run -t --rm okyktenko/sys_metrics:latest mem

### CPU metrics:

docker run -t --rm okyktenko/sys_metrics:latest cpu


