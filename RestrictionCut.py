
# Given a DNA sequence and restriction enzyme, returns the two cut pieces and their lengths

def restriction_fragmentation(SEQUENCE, ENZYME):
    fragment_one = SEQUENCE.find(ENZYME) + 1
    fragment_two = len(SEQUENCE) - fragment_one
    print('\nFragment 1 length: %d \nFragment 2 length: %d \n' % (fragment_one, fragment_two))
    sequence_list = list(SEQUENCE)
    fragment_one_seq = ''.join(sequence_list[:fragment_one])
    fragment_two_seq = ''.join(sequence_list[fragment_one:])
    print('Fragment 1 sequence: %s \nFragment 2 sequence: %s\n' % (fragment_one_seq, fragment_two_seq))
    
print('What is the DNA sequence?')
SEQUENCE = input(' > ').upper()
print('\nWhere is the restriction enzyme cut location (X*YZZ format, cut between X and Y)?')
ENZYME = input(' > ').upper()
restriction_fragmentation(SEQUENCE, ENZYME)