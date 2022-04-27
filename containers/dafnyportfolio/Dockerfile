FROM mcr.microsoft.com/dotnet/sdk:5.0-bullseye-slim

RUN apt-get update && apt-get install -y python3 git python3-pip unzip wget
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip install GitPython

WORKDIR /opt/
RUN wget https://github.com/dafny-lang/dafny/releases/download/v3.4.2/dafny-3.4.2-x64-debian-8.11.zip
RUN unzip dafny-3.4.2-x64-debian-8.11.zip
RUN dotnet tool install --global boogie --version 2.10

WORKDIR /opt/cvc5/
RUN wget https://github.com/cvc5/cvc5/releases/latest/download/cvc5-Linux && mv cvc5-Linux cvc5 && chmod +x cvc5

RUN apt-get update && apt-get install -y z3

WORKDIR /

ENV PATH="/opt/dafny/:/root/.dotnet/tools:/opt/cvc5:$PATH"

COPY dafnyportfolio dafnyportfolio/

ARG COMMIT_HASH
ENV _COMMIT_HASH=$COMMIT_HASH
ENTRYPOINT python3 /dafnyportfolio/src/solve.py --default-args-source Dafny --commit-hash "$_COMMIT_HASH" $0 $@

