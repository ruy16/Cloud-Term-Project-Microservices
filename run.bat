1. Install python
docker run -d -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /developer/project -e DISPLAY=host.docker.internal:0 -p 5000:5000  --name myproject-vscode cmiles74/docker-vscode

docker run -ti --privileged --net=host --pid=host --ipc=host --volume /:/host busybox chroot /host
docker run --rm -e SONAR_HOST_URL="http://localhost:9000" -v "/usr/src" sonarsource/sonar-scanner-cli
mvn sonar:sonar -Dsonar.projectKey=oliver-cool-code -Dsonar.host.url=http://localhost:9000 -Dsonar.login=db4296cd487d770b7095593cd9ec2de954b2d98a
  toolbox-sonarQube-sonarScan-service:
    image: sonarqube
    container_name: sonarqube
    ports:
      - 9000:9000
      - 9092:9092