import csv

with open("stu.csv" , "w") as file:
  writer = csv.writer(file)
  writer.writerow(["Name" , "Class" , "Section" , "Age" , "City"])
  writer.writerow(["vishesh",12,"C",20,"jaipur"])
  writer.writerow(["saksham",11,"B",18,"delhi"])
  writer.writerow(["hardik",10,"A",20,"mumbai"])
  writer.writerow(["khush",8,"D",22,"jaipur"])


with open("stu.csv" , "r") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)
