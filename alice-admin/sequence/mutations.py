def mutated_sequence(sequence, start_position, stop_position, amino_acid):
    '''
    Function name: mutated_sequence
    Arguments: sequence, start_position, stop_position and amono_acid
    Returns: mutated sequence
    Function mutates sequence by concatenating together:
    - the elements in 'sequence' starting from the beginning of the 'sequence' to the
    start_position parameter + 1.
    - value(s) from the amino_acid.
    - the elements in 'sequence' starting from the index specified by the stop_position
    parameter and extending to the end of the 'sequence'.
    '''
    return sequence[:start_position - 1] + amino_acid + sequence[stop_position:]