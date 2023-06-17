import re
from datetime import datetime

import pandas as pd

from cli import cli
from misc import filter
from db import connection, select

if __name__ == "__main__":

    #execution start time
    start_datetime = datetime.now()

    #parsing command line arguments and assigning the flags to variables
    args = cli.parse()
    filePath = cli.get_file(args)
    sourceDatabase = cli.get_database(args)
    organismName = cli.get_organism(args)
    columnName = cli.get_column_name(args)
    outputFile = cli.get_output_path(args)

    print('Connecting to the database')

    #connect to the database
    conn, cur = connection.connect()
    print('Connected successfully')

    print(f'Reading data from {filePath}')

    #read data
    data = pd.read_csv(filePath) if filePath.endswith('csv') else pd.read_excel(filePath) if filePath.endswith('xls') or filePath.endswith('xlsx') else print("Sorry, I can work only on excel or csv files")

    print('Cleaning input data')

    #remove brackets with additional mass of amino acid for each peptide
    data[columnName] = data[columnName].apply(lambda x: re.sub(r'\([^)]*\)', '', x))

    #rename columnName to peptide
    data = data.rename(columns={columnName: 'peptide'})

    #list of columns names
    columns=['protein_id', 'peptide', 'sequence', 'mutation_type', 'mutation', 'position']

    #creating empty dataframe with columns defined above
    df = pd.DataFrame(columns=columns)

    print('Finding peptide sequences in database')

    #iterating over data (dataframe) and setting records as result from function that select
    #mutation based on peptide from table mutation, then cconcatenates empty df with records
    for row in data.itertuples():
        records = select.select_mutation_based_on_peptide(cursor = cur, peptide = row.peptide)
        if not records:
            continue
        df = pd.concat(
            [df, pd.DataFrame(records, columns=columns)], ignore_index=True, axis=0
        )

    print('Checking mutations in peptides')

    #adding column mut_present and filtering records, then retaining rows where column mut_present is equal to 1
    #and dropping columns mut_present and sequence from filtered df
    df['mut_present'] = df[['peptide', 'sequence', 'mutation_type', 'position']].apply(lambda x: filter.filter_records(peptide = x[0],
                                                                                                                        sequence = x[1],
                                                                                                                        m_type = x[2],
                                                                                                                        m_pos = x[3]),
                                                                                                                        axis=1)

    df = df[df['mut_present'] == 1]
    df = df.drop(['mut_present', 'sequence'], axis=1)

    #save output to csv file
    df.to_csv(outputFile, sep=',', index = False)

    end_datetime = datetime.now()

    #duration time
    duration = end_datetime - start_datetime

    print(f'Results saved in {outputFile}. Analysis duration: {duration}')

    conn.close()