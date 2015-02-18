
# Prints files by size in descending order within given directory.
# Given argument value determines how many files are printed.

import sys, os

def dir_files(chosen_dir, amount):
    dir_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + chosen_dir
    print('\nDirectory:', dir_path)
    print('\nFiles:')

    items = {}
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            size = os.stat(dirpath + os.path.sep + f).st_size
            items[f] = size

    i = int(amount)
    print('\n%8s   %s\n' % ('size', 'file'))
    while i > 0:
        top = max(items, key=items.get)
        print('%8s   %s' % (items[top], top))
        del items[top]
        i -= 1
    print()
    


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('\tUsage:  {} amount directory '.format(sys.argv[0]))
        sys.exit()
    chosen_dir = sys.argv[2]
    amount = sys.argv[1]
    dir_files(chosen_dir, amount)