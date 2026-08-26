#  Take three numbers and find the largest.

a = int(input("enter number a-->"))
b = int(input("enter number b-->"))
c = int(input("enter number c-->"))

if (a>b) and (a>c):
  print("a is largest number")
elif (b>a) and (b>c):
  print("b is largest number")
elif (c>a) and (c>b):
  print("c is largest number")
