FROM zaquestion/sonarqube-python

EXPOSE 9000

# Add language plugins
COPY . .
RUN export PATH="./sonar-scanner/bin:$PATH"


