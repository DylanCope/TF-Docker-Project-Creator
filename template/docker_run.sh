sudo service docker start
sleep 1
sudo docker run --runtime nvidia -it --rm --name {codename} -v $(pwd):/tf/project \
	-p :8888:8888 -p :6060:6060 \
	{org}/{codename}:latest
sudo service docker stop
