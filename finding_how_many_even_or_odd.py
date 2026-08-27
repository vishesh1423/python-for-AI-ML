# Find how many even and odd numbers are present in a list.


even=0
odd=0
for i in range(n):
  if marks[i]%2==0:
    even += 1
  else:
    odd += 1

print("even number-->" , even)
print("odd number-->" , odd)
