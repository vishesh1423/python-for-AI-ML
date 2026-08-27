# Find the largest number without using max()

largest = marks[0]

for i in range(len(marks)):
    if marks[i]>largest:
      largest=marks[i]
      
print(largest)
