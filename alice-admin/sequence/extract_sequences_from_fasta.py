import pyfastx

def generate_header_seq_from_fasta(fasta_file):
    '''
    Function name: generate_header_seq_from_fasta
    Arguments: fasta_file
    Yeilds: header, seq (sequence)
    Function yeilds header and sequence by utilizing the Python library- pyfastx, which
    is used for processing fasta files.
    '''
    for header, seq in pyfastx.Fasta(fasta_file, build_index = False):
        yield header, seq