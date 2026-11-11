# Strings

# myString1 = "This is Yo me"
# myString2 = 'This is me "Mohanad"'
# tripleLine = """Yo
# THis
# Is
# me"""
# print(myString1)
# print(myString2)
# print(tripleLine)

# myList = ["Mohamed", "Awad", "Elsayed"]

# print("--".join(myList))


# myString = "hello my neighbor"

# # print(myString.title())
# myString = myString.replace("a", "")
# myString = myString.replace("e", "")
# myString = myString.replace("i", "")
# myString = myString.replace("o", "")
# myString = myString.replace("u", "")

# print(myString)


# myString = "Hello my great HERO"
# count = 0
# for char in myString:
#     if char == " ":
#         None
#     else:
#         count += 1
# print(count)


# myString = "Hello1231 my great Neighbors Hello12S1"

# myList = myString.split()  # ['Hello', 'my', 'great', 'Neighbors']

# longest = 0
# longestWord = ""
# for word in myList:
#     count = 0
#     for char in word:
#         if char == " ":
#             None
#         else:
#             count += 1
#     if count >= longest:
#         longestWord = word
#         longest = count
#     else:
#         None
# print(longestWord)


newPass = input("Enter Your New Password : ")

if not any(c.isupper() for c in newPass):
    print("Passwords Must Contain Upper Cased Letters")
elif not any(c.islower() for c in newPass):
    print("Passwords Must Contain Lower Cased Letters")
elif not any(c.isdigit() for c in newPass):
    print("Password must have a number")
elif any(c.isspace() for c in newPass):
    print("Passwords Can't Contain Spaces")
else:
    print("Password successfully set!")
