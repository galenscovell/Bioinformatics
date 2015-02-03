
#! /usr/bin/env python3

# Calculates G/C content of given FASTA sequence
# Assumes the sequence string is all on one line


from sys import argv


def gc_content(seq):
    total = len(seq)
    gc = 0
    for char in seq:
        if char.upper() in ('G', 'C'):
            gc += 1
    ratio = float(gc / total)
    percentage = round(ratio * 100, 2)
    print('\nSequence Length: ' + str(total) + ' bases')
    print('G/C Content: ' + str(percentage) + '%\n')


if __name__ == '__main__':
    filename = argv[1]
    f = open(filename)
    defline = f.readline()
    sequence = f.readline()
    gc_content(sequence)