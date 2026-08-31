# Write a function that counts the number of vowels in a string.

a = "Vishesh"
count = 0

for i in range(len(a)):
  if a[i] in "AEIOUaeiou":
    count = count +1
print(count)
