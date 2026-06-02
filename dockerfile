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

RUN apt-get update 

CMD ["/bin/bash"]