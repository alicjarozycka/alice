def select_mutation_based_on_peptide(cursor, peptide):
    '''
    Function name: select_mutation_based_on_peptide
    Arguments: cursor, peptide
    Returns: records
    Function takes each peptide provided by the user and checks if peptide can be found in any sequence in mutation table
    if yes, it returns its protein id, sequence, mutation type, mutation and position.
    '''
    peptide_r = f'%{peptide}%'

    records = []

    cursor.execute(
        'SELECT protein_id, sequence, mutation_type, mutation, position FROM mutation WHERE sequence LIKE %s',
        (peptide_r,)
    )

    for record in cursor:
        record_list = [
            record[0], peptide, record[1], record[2], record[3], record[4]
        ]

        records.append(record_list)


    return records