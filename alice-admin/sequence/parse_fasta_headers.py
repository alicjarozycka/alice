from sys import exit

def get_id_from_header(header, sourceDB):
    '''
    Function name: get_if_from_header
    Arguments: header, sourceDB
    Returns: parsed headers
    Function parses header from fasta file. Depending on which database the sequence is from,
    uses function that parses headers. If sourceDB == uniprot, uses parse_uniprot.
    If sourceDB == openprot, uses parse_openprot. It is important because these databases
    have different headers.
    '''
    sourceDB = sourceDB.lower()
    if sourceDB == 'uniprot':
        return parse_uniprot(header)

    if sourceDB == 'openprot':
        return parse_openprot(header)

    print('Sorry, I can only work with OpenProt or UniProt source data!')
    exit(1)

#function that parses uniprot headers
def parse_uniprot(header):
    uniprot_id = header.split('|')[1]
    return uniprot_id

#function that parses openprot headers
def parse_openprot(header):
    openprot_id = header.split('|')[0].replace('>', '')
    return openprot_id