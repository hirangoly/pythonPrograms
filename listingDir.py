# Listing files, sub directory and thier files
# structure - dir1 -> file1.txt, file2.txt dir1>dir2 -> file3.txt, file4.txt dir1>dir3 -> file6.txt dir1>dir2>dir3 -> file5.txt

import os

def listdir(name):
    dir_list = []
    path = os.path.join(name + '/')
    if os.path.isdir(path):
        print name
        for x in os.listdir(path): 
            new_path = path + x           
            if os.path.isdir(new_path):                
                # put in dictionary to call at end of loop
                dir_list.append(new_path)
                # listdir(new_path)
            else:
                print x

        for new_path in dir_list:
            print
            listdir(new_path)
      
name = 'dir1'
listdir(name)
