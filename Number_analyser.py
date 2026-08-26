. # Create a Number Analyzer:

# Input → 25

# Output:
# Positive
# Odd
# Not divisible by 3

a=int(input("enter your number-->"))
print(a)
print("-------------")

if a/a==1:
  print("number is positive")
  print("-------------")
else:
  print("number is negative")
  print("-------------")

if a%2!=0:
  print("the number is odd")
  print("-------------")

if a%3!=0:
  print("the number is not divisible by 3")
