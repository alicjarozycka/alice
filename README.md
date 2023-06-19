# Alice tool

## Table of contents

-   [General info](#general-info)
-   [How to run](#how-to-run)

## General info

Alice tool was created as Bachelor Thesis Project. It was built using Python 3.11.2 version. It does contain two programs and database:

- Alice,
- Alice-admin, 
- AliceDB.

Moreover, it uses Docker to create databse and run Python script. It is important to download [Docker](https://www.docker.com/products/docker-desktop/) with [Compose plugin](https://docs.docker.com/compose/).

## How to run

To use this tool, you should firstly install all required libraries. Being in the project root directory, just type in the terminal:

```
$ pip install -r requirements.txt
```

This command will simply install all external libraries in Python that are used in this project. 

1. The first step is to create a database. In order to do that, go to [alicedb directory](https://github.com/alicjarozycka/alice/tree/master/alicedb) and follow steps given in the alicedb README.
2. Then change the directory to [alice-admin](https://github.com/alicjarozycka/alice/tree/master/alice-admin) and again follow steps from alice-admin README.
3. The last step is to run Alice program. How to do that you can find in [alice README](https://github.com/alicjarozycka/alice/tree/master/alice).
