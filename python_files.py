
# Prints the names of all python files within given directory 
# extending from script root directory.

import sys, os

def dir_files(chosen_dir):
    dir_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + chosen_dir
    print('\nDirectory:', dir_path)
    print('\nPython files:')
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            if f.lower().endswith('.py'):
                print('\t' + os.path.basename(dirpath) + os.path.sep + f)
    print()
    


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('\tUsage:  {} directory'.format(sys.argv[0]))
        sys.exit()
    chosen_dir = sys.argv[1]
    dir_files(chosen_dir)