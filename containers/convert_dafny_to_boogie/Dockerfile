FROM mcr.microsoft.com/dotnet/sdk:5.0-bullseye-slim

RUN apt-get update && apt-get install -y unzip wget

WORKDIR /opt/
RUN wget https://github.com/dafny-lang/dafny/releases/download/v3.4.2/dafny-3.4.2-x64-debian-8.11.zip
RUN unzip dafny-3.4.2-x64-debian-8.11.zip

ENTRYPOINT /opt/dafny/dafny /noVerify /print:$1 $0

