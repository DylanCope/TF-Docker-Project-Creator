sudo service docker start
sleep 1
docker build -t {org}/{codename}:latest .
sudo service docker stop
