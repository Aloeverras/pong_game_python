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

RUN /bin/bash -c "set -eux" && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    sudo \
    libx11-dev \
    libxext-dev \
    libxrandr-dev \
    libxrender-dev \
    libxinerama-dev \
    libxi-dev \
    libxcursor-dev \
    libxss-dev \
    libgl1-mesa-dev \
    ${PACKAGES} && \
    apt-get upgrade && \
    sudo groupadd -g $GROUPID $GROUPNAME && \
    sudo useradd -u ${USERID} -g ${GROUPNAME} -m -s /bin/bash ${USERNAME} && \
    # clean commands \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace   

COPY . .

USER ${USERNAME}  

EXPOSE 8080

CMD ["/bin/bash"]