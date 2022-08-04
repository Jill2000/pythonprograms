print("Submitted by: Donnah May C. Benedicto")

username = ["John","Peter","David"]
password = ["abc123","123abc", "a1b2c3"]

currUsername=input("Username: ")
currPassword=input("Password: ")

for x in range(len(username)):
  if currUsername == username[x] and currPassword == password[x]:
    print("Welcome, " + username[x])
    break
else:
  print("Account not found. ")
