FROM debian:trixie-backports

# argumens 

ARG USERNAME
ARG USERID
ARG GROUPNAME
ARG GROUPID

RUN apt-get update 

CMD ["/bin/bash"]