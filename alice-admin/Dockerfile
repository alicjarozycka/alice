FROM python:3.11.3-buster

RUN apt-get update

RUN wget https://r.mariadb.com/downloads/mariadb_repo_setup
RUN chmod +x mariadb_repo_setup
RUN ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"

RUN apt-get install -y libmariadb3 libmariadb-dev nano
RUN pip3 install mariadb pyfastx requests

WORKDIR /home

ENV DB_USER=root
ENV DB_PASSWORD=pass
ENV DB_HOST=172.16.238.10
ENV DB_PORT=3306
ENV DB_NAME=alicedb

COPY ./ ./

ENTRYPOINT [ "python3", "alice-admin.py", "-f", "data/data.fasta", "-org", "homo_sapiens", "-src", "uniprot" ]
