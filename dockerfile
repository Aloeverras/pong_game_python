FROM debian:trixie-backports

ARG USERNAME
ARG USERID
ARG GROUPNAME
ARG GROUPID

RUN apt-get update 

CMD ["/bin/bash"]