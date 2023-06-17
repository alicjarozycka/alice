import re

def filter_records(peptide, sequence, m_type, m_pos):
    '''
    Function name: filter_records
    Arguments: peptide, sequence, m_type, m_pos
    Returns: 0 or 1
    Firstly this function splits positions for pos_start (start position) and pos_end (end position).
    Then removes all whitespace characters and changes pos_start and pos_end to integers. If mutation
    type is Deletion, the value of pos_start is assigned to pos_end. Otherwise for each peptide checks
    its length and adds 1 to this value, chcecks start position and adds it to start_positions list.
    Later iterates over start_positions list and adds 1 to each start_position value. Start_position
    value plus peptide_len is assigned to end_position. If start_position is less than or equal to
    pos_start and end_position is greater than or equal to pos_end returns 1, otherwise 0.
    '''
    pos_start, pos_end = m_pos.split('->')

    pos_start = int(pos_start.strip())
    pos_end = int(pos_end.strip())

    if m_type == 'Deletion':
        pos_end = pos_start

    peptide_len = len(peptide) + 1
    start_positions = [m.start() for m in re.finditer(peptide, sequence)]

    for start_position in start_positions:
        start_position += 1
        end_position = start_position + peptide_len

        if start_position <= pos_start and end_position >= pos_end:
            return 1

    return 0