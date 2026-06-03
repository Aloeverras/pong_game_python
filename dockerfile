FROM debian:trixie-backports

# env variables

# labels

# argumens 

ARG USERNAME
ARG USERID
ARG GROUPNAME
ARG GROUPID
ARG PACKAGES

# running dockerfile

RUN apt-get update && \
    apt-get install -y --no-recommendes sudo ${PACKAGES} && \
    apt-get upgrade && \
    sudo groupadd -g $GROUPID $GROUPNAME && \
    sudo useradd -u ${USERID} -g ${GROUPNAME} -m -s /bin/bash ${USERNAME}

CMD ["/bin/bash"]