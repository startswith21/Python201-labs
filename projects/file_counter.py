# Add the code for the file counter script that you wrote in the course.
#count number of files by extension in dictionary: filename=key, number=value
import pathlib
import pprint
import os


path = pathlib.Path().cwd()
str(path)
print(path)

Desktop = pathlib.Path("/Users/xxx/Desktop/")
for filepath in Desktop.iterdir():
    print(filepath.name)
    print(filepath.suffix)

for filepath in Desktop.iterdir():
    filetype = filepath.suffix
    print(filetype)
    print(type(filetype))   
#------
from os.path import join, splitext
from glob import glob
from collections import Counter

desktop1 = pathlib.Path("/Users/xxx/Desktop/")

c = Counter([splitext(i)[1][1:] for i in glob(join(desktop1, '*'))])
for ext, count in c.most_common():
    print(ext, count)
    print(type(count))
   

 






        




