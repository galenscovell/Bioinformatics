
# Prints names of all files within given directory 
# that were created after given date (YYYY-MM-DD).


import sys, os, time

def dir_files(chosen_dir, chosen_date):
    dir_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + chosen_dir
    print('\nDirectory:', dir_path)

    print('Filter date:', chosen_date)
    date_to_int = int(chosen_date.replace('-', ''))
    
    print('\nFiles:')
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            f_create = time.localtime(os.path.getctime(os.path.join(dirpath, f)))
            format_create = time.strftime('%Y-%m-%d', f_create)
            create_to_int = int(format_create.replace('-', ''))

            if create_to_int > date_to_int:
                f_mod = time.localtime(os.path.getmtime(os.path.join(dirpath, f)))
                format_mod = time.strftime('%Y-%m-%d', f_mod)
                print('\t' + format_mod, os.path.basename(dirpath) + os.path.sep + f)

    print()
            


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('\tUsage:  {} directory YYYY-MM-DD'.format(sys.argv[0]))
        sys.exit()
    chosen_dir = sys.argv[1]
    chosen_date = sys.argv[2]
    dir_files(chosen_dir, chosen_date)