FROM tensorflow/tensorflow:2.7.0-gpu-jupyter
RUN python -m pip install --upgrade pip
COPY requirements.txt ./requirements.txt
RUN python -m pip install -r requirements.txt 
ENV PYTHONPATH="/tf/project:$PYTHONPATH"
RUN rm -rf tensorflow-tutorials
