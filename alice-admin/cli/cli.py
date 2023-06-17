import os
import argparse

#check if the input file provided by the user exists
def check_if_file_exists(file):
    if not os.path.exists(file):
        raise argparse.ArgumentTypeError(f"{file} does not exist")
    return file

#parse command-line arguments - 3 flags that are described below
def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required = True, type = check_if_file_exists, help='Path to your fasta file')
    parser.add_argument('-org', '--organism', required = True, help='From which organism is your data')
    parser.add_argument('-src', '--source', required = True, help='From which database is your data')
    args = parser.parse_args()
    return args

def get_fasta_file(args):
    fasta_file = args.file
    return fasta_file

def get_database_from_args(args):
    database = args.source
    return database

def get_organism_from_args(args):
    organism = args.organism
    return organism