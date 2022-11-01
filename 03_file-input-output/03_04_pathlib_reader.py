# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
import pathlib
from pathlib import Path
import pprint 
import csv
dictionary = {"pdf": 0, "png": 0, "python":0, "docx": 0}
pdf_files = 0
png_files = 0
python_files = 0
docx_files = 0

desktop = pathlib.Path("/Users/xxx/Desktop/")

for filepath in desktop.iterdir():
    if filepath.suffix == ".pdf":
        dictionary["pdf"] += 1
    
    if filepath.suffix == ".png":
        dictionary["png"] += 1
    
    if filepath.suffix == ".py":
        dictionary["python"] += 1

    if filepath.suffix == ".docx":
        dictionary["docx"] += 1
print(dictionary)

#writing to csv file using pathlib:

with open ("counting.csv", "w") as csvdict:
    filecounter = csv.writer(csvdict)
    data = [dictionary["docx"], dictionary["python"], dictionary["png"], dictionary["pdf"]]
    filecounter.writerow(data)
    
data_path = Path("/Users/xxx/Desktop")

with open (data_path.joinpath("counting.csv"), "a") as fileapp:
    filecounter = csv.writer(fileapp)
    data = [dictionary["docx"], dictionary["python"], dictionary["png"], dictionary["pdf"]]
    filecounter.writerow(data)
    
with open (data_path.joinpath("counting.csv"), "r") as readfile:
    print(readfile.read())
