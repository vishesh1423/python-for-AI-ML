# Count how many numbers in a list are greater than 50.

list = [10,20,99,55,77,33]
n = len(list)

for i in range(n):
  if list[i] > 50:
    print("the number is greater than 50-->" , list[i])
