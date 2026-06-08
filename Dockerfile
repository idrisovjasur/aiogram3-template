FROM ubuntu:latest
LABEL authors="idris"

ENTRYPOINT ["top", "-b"]