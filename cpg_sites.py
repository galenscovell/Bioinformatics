
#! /usr/bin/env python3

# Determines content of FASTA sequence, expected/actual CpG sites
# Assumes the sequence string is all on one line


from sys import argv


def cpg_sites(seq):
    seq_length = 0
    content_dict = { 'C': 0, 'G': 0, 'CG': 0 }
    for char in seq:
        if char.upper() in ('C', 'G'):
            content_dict[char] += 1
        seq_length += 1
    content_dict['CG'] = seq.count('CG')
    c_ratio = round(content_dict['C'] / seq_length, 3)
    g_ratio = round(content_dict['G'] / seq_length, 3)
    expected_cpg = round(c_ratio * g_ratio * seq_length)
    print('\nSequence Length: ' + str(seq_length))
    print('C: ' + str(content_dict['C']) + ', ' + str(c_ratio))
    print('G: ' + str(content_dict['G']) + ', ' + str(g_ratio))
    print('CpG (expected): ' + str(expected_cpg))
    print('CpG (actual): ' + str(content_dict['CG']) + '\n')


if __name__ == '__main__':
    filename = argv[1]
    f = open(filename)
    defline = f.readline()
    sequence = f.readline()
    cpg_sites(sequence)