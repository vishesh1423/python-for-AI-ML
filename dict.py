marks = {
    "maths" : 50 ,
    "science" : 75 , 
    "english" : 60
}

total=0

for subject in marks.keys():
  total = total +marks[subject]

print(total)
