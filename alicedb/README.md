# AliceDB

## How to create database

To create AliceDB, you have to change directory to alicedb. Then using Docker command, type in the terminal:

```
$ docker compose up -d
```

This command will create and run database, the whole process will be running in the background (-d flag). There will be created container that consists of two containers:
- alicedb
- adminer-1.

To create container, Docker image is required. The aforementioned command also downloads latest adminer image and mariadb 10.11 release from Docker Hub.

You can check if these images are downloaded, by command:

```
$ docker image ls
```
