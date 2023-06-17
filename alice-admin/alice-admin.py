import json
import requests
from datetime import datetime

from cli import cli
from db import connection, insert
from misc import type_of_mutation
from sequence import extract_sequences_from_fasta, parse_fasta_headers, mutations

if __name__ == "__main__":

    #execution start time
    start_datetime = datetime.now()

    #parsing command line arguments and assigning the flags to variables
    args = cli.parse()
    fastaPath = cli.get_fasta_file(args)
    sourceDatabase = cli.get_database_from_args(args)
    organismName = cli.get_organism_from_args(args)

    print('Connecting to the database')

    #connect to the database
    conn, cur = connection.connect()
    print('Connected successfully')

    ##### TO REMOVE AFTER DEVELOPMENT
    cur.execute("DELETE FROM protein")
    cur.execute("DELETE FROM mutation")

    #iterating over header and seq (sequence) using function generate_header_seq_from_fasta
    #and assigning id from header to recordId variable, then function inserting sequence, recordId,
    #sourceDatabase and organismName is used to fill table protein in database
    for header, seq in extract_sequences_from_fasta.generate_header_seq_from_fasta(fasta_file = fastaPath):
        recordId = parse_fasta_headers.get_id_from_header(header = header, sourceDB = sourceDatabase)
        print(f"Working on {recordId}")

        insert.insert_protein(cursor = cur,
                            sequence = seq,
                            id = recordId,
                            source = sourceDatabase,
                            organism = organismName)

        #mutations are avaliabe only for uniprot, so if sourceDatabase = uniprot, send request
        #to proteins api using recordId, if response code is 200, convert json-formatted data
        #to python objects
        if sourceDatabase == 'uniprot':
            proteins_api_resp = requests.get(f'https://www.ebi.ac.uk/proteins/api/proteins/{recordId}')

            if not proteins_api_resp.ok:
                continue

            proteins_api_data = json.loads(proteins_api_resp.text)
            try:
                #Iterating over features in the response, if type==VARIANT, then get all necessary informations like
                #start and stop position of mutation, amino_acid and description. Mutating sequence using mutated_sequence
                #and then inserting all the previously mentioned information into a table mutation
                for feature in proteins_api_data['features']:
                    if feature['type'] == 'VARIANT':
                        start_position = int(feature['begin'])
                        stop_position = int(feature['end'])
                        amino_acid = 'missing' if feature['alternativeSequence'] == '' else feature['alternativeSequence']
                        description = feature['description']
                        mutant = mutations.mutated_sequence(sequence = seq,
                                                            start_position = start_position,
                                                            stop_position = stop_position,
                                                            amino_acid = feature['alternativeSequence'])
                        try:
                            insert.insert_mutation(cursor = cur,
                                                sequence = mutant,
                                                protein_id = recordId,
                                                mutation = (seq[start_position-1] + ' > ' + amino_acid),
                                                position = (str(start_position) + ' -> ' + str(stop_position)),
                                                mutation_type = type_of_mutation.mutation_type(seq = seq, alternativeSequence = mutant),
                                                description = description)

                        except IndexError:
                            pass
            except KeyError:
                pass

        conn.commit()



    conn.commit()
    conn.close()

    #execution end time
    end_datetime = datetime.now()

    #duration time3
    duration = end_datetime - start_datetime

    print(f'Succesfully added all protein sequences and mutations to the database. It took: {duration}')