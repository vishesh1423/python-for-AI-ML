file = open("vishesh.txt" , "w")
file.write("hardik\n")
file.write("saksham\n")
file.write("prateek\n")
file.close()

file = open("vishesh.txt" , "r")
data = file.read()
print(data)
file.close()


file = open("vishesh.txt" , "r")
data = file.readline()
print(data)
file.close()


file = open("vishesh.txt" , "r")
data = file.readline()
print(data)
data = file.readline()
print(data)
file.close()


file = open("vishesh.txt" , "r")
data = file.readlines()
print(data)
file.close()


for line in data:
  print(line)


file = open("vishesh.txt" , "r")
for line in file:
  print(line)

file.close()



file = open("vishesh.txt" , "r")
for line in file:
  print(line , end = "")

file.close()



file = open("vishesh.txt" , "a")
file.write("\nkhush")
file.close()

file = open("vishesh.txt" , "r")
for line in file:
  print(line)
file.close()



file = open("vishesh.txt" , "r")
for line in file:
  print(line)
file.close()



file = open("vishesh.txt" , "a")
file.write("\nvishesh")
file.close()

file = open("vishesh.txt" , "r")
for line in file:
  print(line)
file.close()



with open ("vishesh.txt" , "r") as file:
  print(file.read())



with open("me.txt" , "w") as file:
  file.write("vishesh ")

with open("me.txt" , "a") as file:
  file.write("sundarwal")

with open("me.txt" , "r") as file:
  print(file.read())
