# AliceDB

## How to create database

To create AliceDB, you have to be in the alicedb directory (here). Then using Docker, type in the terminal:

```
$ docker compose up -d
```

This command will create database and run container that consists of:
- alicedb
- adminer-1.

To create container, Docker image is required. The aforementioned command downloads latest adminer image and mariadb 10.11 release.

You can check if these images are downloaded, by command:

```
$ docker image ls
```
