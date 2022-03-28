import os

"""
Renames the filenames within the same directory
"""

path =  os.getcwd()
filenames = os.listdir(path)

from_str = str(input("from > "))
to_str   = str(input("to   > "))

for filename in filenames:
    try:
        os.rename(filename, filename.replace(from_str, to_str))
    except FileExistsError:
        print("File " + filename + "exists")

print("Successful")
