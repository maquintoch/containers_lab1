FROM kalilinux/kali-rolling
RUN apt-get update
RUN apt-get install -y curl hydra nmap openssh-client
COPY users.txt .
COPY passwords.txt .
ENTRYPOINT /bin/bash