# Keep asking for a password until the correct password is entered.

password = ""
while password != "vishesh@123":
  password = input("enter your password: ")
  if password == "vishesh@123":
    print("correct password")
  else:
    print("wrong password, try again")
