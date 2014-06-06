
# Given a DNA sequence, returns the content of given nucleotide

def contentCalculation(nucleotide, sequence):
    print('\nCalculating content of %s in sequence.\n' % nucleotide)
    content = sequence.count(nucleotide)
    total_length = len(sequence)
    ratio = (content / total_length) * 100
    print('Sequence length: %d \nNucleotide Amount: %d \nPercentage: %f\n' % (total_length, content, ratio))

def nucleotideChoice(nucleotide, sequence):
    while nucleotide != 'A' and nucleotide != 'C' and nucleotide != 'T' and nucleotide != 'G': 
        print('What is the nucleotide of interest?')
        nucleotide = input(' > ').upper()
    contentCalculation(nucleotide, sequence)

print('What is the DNA sequence of interest?')
sequence = input(' > ').upper()
print('DNA sequence:\n %s\n' % sequence)
nucleotide = ' '
nucleotideChoice(nucleotide, sequence)