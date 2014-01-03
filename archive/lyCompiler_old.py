import os
import re
path = raw_input("Enter path of compilation target: ")
splitpath = path.split(r"/")
filename = splitpath[len(splitpath) - 1]
print filename
filenamenoext = filename.split(r".")
list.pop()
# startfile(path)

