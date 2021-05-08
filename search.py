#!/usr/bin/python3

import os
import glob
filename = input("Filename: ")

for root, dirs, files in os.walk(os.getcwd()):
    
    if glob.glob(os.path.join(root,f"*{filename}*")):
        print("Current path:  ", root)
        print()    
        print("Directories:  ", dirs)
        print()
        print("Files:  ", files)
        print("-------------------------------------")



