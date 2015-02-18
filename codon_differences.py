
#! /usr/bin/env python3

# Scans two FASTA sequences for differences in codons
# Uses csv file with amino acid designations to determine
#   amount of synonymous/nonsynonymous differences



from sys import argv


def seq_difference(seq1, seq2):
    gc = read_code('universal.csv')
    syn, non_syn, i = 0, 0, 0
    print('\nSequence differences:')
    while i < len(seq1):
        seq1_frame = seq1[i:i+3]
        seq2_frame = seq2[i:i+3]
        if seq1_frame != seq2_frame:
            if gc[seq1_frame] == gc[seq2_frame]:
                print('%6s' % str(i) + ': ' + seq1_frame, gc[seq1_frame] + ' -> ' + seq2_frame, gc[seq2_frame])
                syn += 1
            else:
                print('%6s' % str(i) + ': ' + seq1_frame, gc[seq1_frame] + ' -> ' + seq2_frame, gc[seq2_frame])
                non_syn += 1
        i += 3
    print('\nTotal differences: ' + str(syn + non_syn))
    print('\t' + str(syn) + ' synonymous')
    print('\t' + str(non_syn) + ' nonsynonymous\n')


def read_code(fn):
    with open(fn) as f:
        return { x[0] : x[1] for x in [ s.split(',') for s in f.readlines() ] }



if __name__ == '__main__':
    filename = argv[1]
    f = open(filename)
    defline_1 = f.readline()
    sequence_1 = f.readline()
    defline_2 = f.readline()
    sequence_2 = f.readline()
    seq_difference(sequence_1, sequence_2)