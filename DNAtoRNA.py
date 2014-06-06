
# Given a DNA sequence, returns the transcribed RNA

def transcribeRNA(SEQUENCE):
    RNA = SEQUENCE.replace('T', 'U')
    print('%s' % RNA)

SEQUENCE = input('DNA sequence: ').upper()
transcribeRNA(SEQUENCE)