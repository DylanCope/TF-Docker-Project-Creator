# TF-Docker Project Creator

Python script to create a project from a template given the following project parameters:

* Author (required)
* Project Name (required)
* Project Codename (derived from project name if not given)
* Org (derived from author if not given)

The script will copy the template repository structure to a new folder located at `../{codename}`.

## Template structure

The template project has the following structure:
```
├── data                    # Contains data files
├── {codename}              # Python module 
├── notebooks               # Jupyter notebooks
├── requirements.txt        # pip requirements for building docker environment
├── Dockerfile              # Extends tensorflow/tensorflow:2.7.0-gpu-jupyter
├── docker_build.sh         # Script for building container
├── docker_run.sh           # Script for starting container and exposing Jupyter to localhost
└── README.md
```

## Running the `project.create` script

From the root of this repository run:
```console
> python -m project.create
```
You will be prompted to fill in the project parameters. 
Otherwise, you can provide any of the parameters via run parameters to the script, usage describe by the help:
```console
> python -m project.create -h
usage: create.py [-h] [--no-interactive] [-author AUTHOR] [-project PROJECT] [-codename CODENAME] [-org ORG]

optional arguments:
  -h, --help          show this help message and exit
  --no-interactive    Do not prompt user for parameters (all parameters must be provided via commandline)
  -author AUTHOR      Author of the project (required)
  -project PROJECT    Name of the project (required)
  -codename CODENAME  Short codename for project (optional)
  -org ORG            Organisation responsible for the project (optional)
```

## Development

Once the project has been created, navigate to the newly generated folder (`../{codename}`).

### Setting up the Docker container

Run the `docker_build.sh` script. Note that this extends from a GPU-ready Tensorflow docker image and therefore you must make sure you have [configured your docker correctly](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). If you do not have a CUDA-compatibile GPU then you should remote the `-gpu` tag from the Dockerfile.

### Running the code

Run the `docker_run.sh` file to start the container. Copy the Jupyter token from the terminal and navigate to `localhost:8888` on your browser. Paste the Jupyter token into the page (and optionally set-up a password if you intend to leave the server running). 

You can then develop in the Jupyter environment. You can create Jupyter notebooks in the `notebooks` folder or Python files in the Python module folder (which can then be imported in notebooks with `import {codename}` as the Dockerfile adds the module to the `PYTHONPATH`).
