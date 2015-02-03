
#! /usr/bin/env python3

# Scans two FASTA sequences for differences in bases



from sys import argv


def seq_difference(seq1, seq2):
    if len(seq1) != len(seq2):
        print('Sequence lengths differ.')
        return None
    i = 0
    diff_count = 0
    print('\nSequence differences:')
    while i < len(seq1):
        if seq1[i] != seq2[i]:
            print('%6s' % str(i) + ': ' + seq1[i] + ' -> ' + seq2[i])
            diff_count += 1
        i += 1
    print('\nTotal differences: ' + str(diff_count))
    percentage = round(100 - (100 * diff_count / len(seq1)), 2)
    print(str(percentage) + '% identical\n')



if __name__ == '__main__':
    filename = argv[1]
    f = open(filename)
    defline_1 = f.readline()
    sequence_1 = f.readline()
    defline_2 = f.readline()
    sequence_2 = f.readline()
    seq_difference(sequence_1, sequence_2)