# tensorflow with noVNC
FROM debian:buster
#Python
RUN set -ex; \
    apt-get update; \
    apt-get -y install sudo; \
    sudo apt -y update; \
    sudo apt -y install \
      python3-dev \
      python3-pip \
      python3-venv

#virtual environment 
RUN python3 -m venv --system-site-packages ./venv
#!/bin/bash source ./venv/bin/activate  
RUN pip3 install --upgrade pip
RUN pip3 list  

#Install tensor
RUN pip3 install --upgrade tensorflow
RUN python3 -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

# Install git, supervisor, VNC, & X11 packages
RUN set -ex; \
    apt-get update; \
    apt-get install -y \
      bash \
      fluxbox \
      net-tools \
      novnc \
      supervisor \
      x11vnc \
      xterm \
      xvfb

# Setup demo environment variables
ENV HOME=/root \
    DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    DISPLAY=:0.0 \
    DISPLAY_WIDTH=1024 \
    DISPLAY_HEIGHT=768 \
    RUN_XTERM=yes \
    RUN_FLUXBOX=yes
COPY . /app
CMD ["./app/entrypoint.sh"]
EXPOSE 8080
