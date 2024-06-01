FROM ubuntu:latest
LABEL authors="decadenz"

ENTRYPOINT ["top", "-b"]