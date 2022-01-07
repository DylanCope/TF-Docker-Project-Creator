# {project}


{author}, {date}

---

## Project Root Structure

```
.
├── data                    # Contains data files
├── {codename}{spaces}# Python module 
├── notebooks               # Jupyter notebooks
├── docker-requirements.txt # pip requirements for building docker environment
├── Dockerfile              # Extends tensorflow/tensorflow:2.7.0-gpu-jupyter
├── docker_build.sh         # Script for building container
├── docker_run.sh           # Script for starting container and exposing Jupyter to localhost
└── README.md
```

## Building the environment

### Setting up the container

Run the `docker_build.sh` script. Note that this extends from a GPU-ready Tensorflow docker image and therefore you must make sure you have [configured your docker correctly](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). If you do not have a CUDA-compatibile GPU then you should remote the `-gpu` tag from the Dockerfile.

## Running the code

Run the `docker_run.sh` file to start the container. Copy the Jupyter token from the terminal and navigate to `localhost:8888` on your browser. Paste the Jupyter token into the page (and optionally set-up a password if you intend to leave the server running). 
