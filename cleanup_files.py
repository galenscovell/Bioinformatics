
# Deletes all files with extensions (.aux .idx .ilg .ind .log .synctex.gz .toc)
# within specified directory.

import sys, os

def dir_files(chosen_dir):
    dir_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + chosen_dir
    print('\nDirectory:', dir_path)
    print('\nFiles:')
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            exts = ('.aux', '.idx', '.ilg', '.ind', '.log', '.synctex.gz', '.toc')
            if f.lower().endswith(exts):
                print('\tRemoving: ' + os.path.basename(dirpath) + os.path.sep + f)
                os.remove(dirpath + os.path.sep + f)
    print()
    


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('\tUsage:  {} directory'.format(sys.argv[0]))
        sys.exit()
    chosen_dir = sys.argv[1]
    dir_files(chosen_dir)