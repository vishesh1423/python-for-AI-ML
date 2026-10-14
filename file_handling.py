with open("me.txt" , "w") as file:
  file.write("vishesh ")

with open("me.txt" , "a") as file:
  file.write("sundarwal")

with open("me.txt" , "r") as file:
  print(file.read())
