def mutation_type(seq, alternativeSequence):
    '''
    Funtion name: mutation_type
    Arguments: seq (sequence) and alternativeSequence
    Returns: mut_type (mutation type)
    Function checks lengths of original sequence (seq) and mutated sequence (alternativeSequence).
    If lengths are equal, returns 'SNP'. If original sequences length is greater than alsternativeSequence
    returns 'Deletion'. Otherwise returns 'Insertion'
    '''
    seq_len = len(seq)
    alt_seq_len = len(alternativeSequence)

    if seq_len == alt_seq_len:
        mut_type =  "SNP"
    elif seq_len > alt_seq_len:
        mut_type = 'Deletion'
    elif seq_len < alt_seq_len:
        mut_type = 'Insertion'

    return mut_type