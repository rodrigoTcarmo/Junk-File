# Software created for check repeated files inside directories

import os
import uuid

main_path = r'C:\Users\rodri\Documents\GitHub\Junk File\test'
file_key = {}


def verify_files():
    for root, dirs, files in os.walk(main_path):
        for file in files:
            avoid_file = os.path.join(root, file)
            print(avoid_file)

            
        print('\n')


if __name__ == "__main__":
    verify_files()
