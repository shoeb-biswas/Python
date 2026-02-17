from pathlib import Path
import csv

Data_Path = Path('data2')
Data_Path.mkdir(exist_ok=True)
csv_path = Data_Path / "student.csv"

# Write
with csv_path.open('w', newline="",encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerow(["Name", "Age"])
  writer.writerow(["Rakib", 20])
  writer.writerow(["Takib", 40])
  writer.writerow(["Yakib", 25])

# Read
with csv_path.open('r',encoding="utf-8") as f:
  reader =  csv.reader(f)
  print(list(reader))
