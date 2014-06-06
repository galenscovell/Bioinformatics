
# Given a DNA sequence, returns counts of each nucleotide amount

def nucleotideCount(SEQUENCE):
    adenine = SEQUENCE.count('A')
    cytosine = SEQUENCE.count('C')
    guanine = SEQUENCE.count('G')
    thymine = SEQUENCE.count('T')
    print('%d %d %d %d' % (adenine, cytosine, guanine, thymine))

SEQUENCE = input('DNA sequence: ').upper()
nucleotideCount(SEQUENCE)