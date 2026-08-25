# Take two numbers as input.
# Take an operator as input: +, -, *, /
# Perform the selected operation.
# Print the result.
# If the user enters an invalid operator, print Invalid Operator.
# If the user tries to divide by zero, print Cannot divide by zero.

# that's called algorithm of code.


a = float(input(" enter your number a --> "))
b = float(input(" enter your number b --> "))
operator = input("enter your operator---> ")
c = a+b
d = a-b
e = a*b
f = a/b
if operator == "+":
  print(c)
  print("--------------------------------")
elif operator == "-":
  if a-b==c:
    print(d)
  else:
    print(-d)
  print("--------------------------------")
elif operator == "*":
  print(e)
  print("--------------------------------")
elif operator == "/":                                   # if we taking float number that means it can not be divided by zero
  if b==0:
    print("cannot divided by zero")
  else:
    print(f)
  print("--------------------------------")
