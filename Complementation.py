
# Returns a complementary or reversed strand given a DNA sequence

def complement_or_reverse(SEQUENCE):
    print('\nComplement or reverse?')
    choice = input(' > ').lower()
    if choice.startswith('c'):
        complement_strand(SEQUENCE)
    elif choice.startswith('r'):
        reverse_strand(SEQUENCE)

def complement_strand(SEQUENCE):
    complement1 = SEQUENCE.replace('A', 't')
    complement2 = complement1.replace('C', 'g')
    complement3 = complement2.replace('G', 'c')
    complement4 = complement3.replace('T', 'a')
    print(complement4.upper())

def reverse_strand(SEQUENCE):
    sequence_list = list(SEQUENCE)
    final_reversed = ''.join(sequence_list[::-1])
    print(final_reversed)
    
print('What is the DNA sequence of interest?')
SEQUENCE = input(' > ').upper()
complement_or_reverse(SEQUENCE)