# Alice

The purpose of Alice program is to identify peptides which may contain sequences of naturally observed variants.

Table of the arguments below, shows required flags to properly execute the script.

| Argument | Parameter description | Is the argument required? |
| :-----: | :---: | :---: |
| -f | Path to the input file (csv, xlsx, xls) | Yes |
| -src | Name of the database (eg. UniProt) | Yes |
| -org | Name of the organism from which the data comes | Yes | 
| -col | Column name in the input file indicating location of the peptide sequences | Yes |
| -out | Path and desired output file name | Yes |

To run the Alice program, move to alice directory and then enter in the command line:
```
$ py alice.py -f path_to_input_file -org organism_name -src source_database -col column_name -out path_and_output_filename
```

This command will start a database search, using sequences from the user's input file. 

Search results will be saved to the output file in the specific location with user-defined file name. 
