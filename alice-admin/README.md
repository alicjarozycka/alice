# Alice-admin

To add data to AliceDB, you have to change directory to alice-admin. Then using Docker command, type in the terminal:

```
$ docker build -t aliceadmin:0.1 .
```

This will build a docker image named aliceadmin with tag 0.1.

Docker image is used to run Python script from alice-admin.py. The following step is to run a container and add data to the database.

```
$ docker run --name aliceadmin -d --network alicedb_alice_network -v path_to_data:/home/data aliceadmin:0.1
```
The command above runs container named aliceadmin, this action initiates adding data to the database.

Make sure that you have stable internet connection because program sends requests to Proteins API in order to obtain information about natural variants.

Dockerfile includes an instruction that automatically starts the program. Pay attention to the arguments included in the Dockerfile.

| Argument | Parameter description | Is the argument required? |
| :-----: | :---: | :---: |
| -f | Path to the input file | Yes |
| -src | Name of the database the file comes from | Yes |
| -org | Name of the organism from which the data comes | Yes | 

In this project, data from UniProt containing sequences from *Homo sapiens* organism were added to the database. By default those parameters were set in the Dockerfile. 
