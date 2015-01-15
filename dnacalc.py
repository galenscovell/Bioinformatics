

# Given a DNA sequence, prints content of given nucleotide
# Either cmdline argument or prompt for input.
# (Default is cmdline argument)

# Usage: python dnacalc.py [arg1] [arg2]
#     arg1: sequence (upper/lowercase, removes non-ATCG characters)
#     arg2: nucleotide to analyze (upper/lowercase, if > 1 character entered uses first)


import sys


def contentCalculation(seq, nt):
    print('\nCalculating %s content in: \n%s\n' % (nt, seq))
    nt_content = seq.count(nt)
    total_length = len(seq)
    ratio = (nt_content / total_length) * 100
    print('\tSequence length: %d \n\tNucleotide Amount: %d \n\tPercentage: %.2f\n' % (total_length, nt_content, ratio))

def nucleotideChoice():
    nucleotide = ' '
    while nucleotide[0] not in ('A', 'T', 'C', 'G'): 
        print('What is the nucleotide of interest?')
        nucleotide = input(' > ').upper()
    return nucleotide[0]

def filterSequence(seq):
    filtered_sequence = []
    for character in seq:
        if character in ('A', 'T', 'C', 'G'):
            filtered_sequence.append(character)
    return ''.join(filtered_sequence)

def promptInput():
    print('\nWhat is the DNA sequence of interest?')
    sequence = input(' > ').upper()
    sequence = filterSequence(sequence)
    print('\nFiltered sequence: %s\n' % sequence)
    contentCalculation(sequence, nucleotideChoice())
    sys.exit()


def main():
    # Uncomment only the following line to run prompt input
    # promptInput()

    if len(sys.argv) == 3:
        sequence, nucleotide = sys.argv[1].upper(), sys.argv[2][0].upper()
        contentCalculation(filterSequence(sequence), nucleotide)
    else:
        print("\n\tTwo arguments required (sequence, nucleotide).\n")
        sys.exit()


if __name__ == '__main__':
    main()