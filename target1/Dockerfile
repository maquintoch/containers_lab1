FROM ubuntu
RUN apt-get update
RUN apt-get install -y openssh-server
RUN echo "root:password" | chpasswd
RUN echo "PermitRootLogin yes">> /etc/ssh/sshd_config
ENTRYPOINT service ssh start && /bin/bash
