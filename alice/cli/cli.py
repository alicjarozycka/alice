import os
import argparse

#check if the input file provided by the user exists
def check_if_file_exists(file):
    if not os.path.exists(file):
        raise argparse.ArgumentTypeError(f"{file} does not exist")
    return file

#parse command-line arguments - 5 flags that are described below
def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required = True, type = check_if_file_exists, help='Path to your csv or excel file')
    parser.add_argument('-org', '--organism', required = True, help='From which organism is your data')
    parser.add_argument('-src', '--source', required = True, help='From which database is your data')
    parser.add_argument('-col', '--column', required = True, help='Column name in your file that contains peptide sequences')
    parser.add_argument('-out', '--output', required = True, help='Path to output file')
    args = parser.parse_args()
    return args

def get_file(args):
    file = args.file
    return file

def get_database(args):
    database = args.source
    return database

def get_organism(args):
    organism = args.organism
    return organism

def get_column_name(args):
    col_name = args.column
    return col_name

def get_output_path(args):
    output_name = args.output
    return output_name
