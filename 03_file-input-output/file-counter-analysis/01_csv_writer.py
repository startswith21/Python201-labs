# Add your file counter code here.
# Then add more code that writes the file counts to a `.csv` file.
import pathlib
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

with open ("filecounts1.csv", "a") as csvfile1:
    writecount = csv.writer(csvfile1)
    data = [dictionary["docx"], dictionary["python"], dictionary["png"], dictionary["pdf"]]
    writecount.writerow(data)
