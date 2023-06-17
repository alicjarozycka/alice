def insert_protein(cursor, sequence, id, source, organism):
    '''
    Function name: insert_protein
    Arguments: cursor, sequence, id (protein id), source (database) and organism
    This function inserts into protein table sequence, id, source database and organism name.
    '''
    cursor.execute(
        "INSERT INTO protein (sequence,id,source,organism) VALUES (?,?,?,?) ON DUPLICATE KEY UPDATE id=id",
        (sequence, id, source, organism))


def insert_mutation(cursor, sequence, protein_id, mutation, position, mutation_type, description):
    '''
    Function name: insert_mutation
    Arguments: cursor, sequence, protein_id, mutation, position, mutation_type and description
    Function inserts into mutation table: mutated sequences, protein id (uniprot), information about
    the change that occured in the sequence, positions where mutation was observed, type of mutation
    and description.
    '''
    cursor.execute(
        "INSERT INTO mutation (sequence, protein_id, mutation, position, mutation_type, description) VALUES (?,?,?,?,?,?)",
        (sequence, protein_id, mutation, position, mutation_type, description)
    )