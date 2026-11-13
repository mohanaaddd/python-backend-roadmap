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


# newPass = input("Enter Your New Password : ")

# if not any(c.isupper() for c in newPass):
#     print("Passwords Must Contain Upper Cased Letters")
# elif not any(c.islower() for c in newPass):
#     print("Passwords Must Contain Lower Cased Letters")
# elif not any(c.isdigit() for c in newPass):
#     print("Password must have a number")
# elif any(c.isspace() for c in newPass):
#     print("Passwords Can't Contain Spaces")
# else:
#     print("Password successfully set!")


# newPass = input("Enter Your New Password : ")

# if len(newPass) < 8:
#     print("Password has to be at least 8 chars")
# elif not any(c.isupper() for c in newPass):
#     print("No upper letters found")
# elif not any(c.islower() for c in newPass):
#     print("No lower letters found")
# elif not any(c.isdigit() for c in newPass):
#     print("Must contain at least 1 number")
# elif any(c.isspace() for c in newPass):
#     print("Can't contain Spaces")
# else:
#     print("DOne")

# mySentence = "Hello my great absolute Neighbors"

# myList = mySentence.split()
# count = 0
# for word in myList:
#     if len(word) > count:
#         count = len(word)
#         longestWord = word
#     else:
#         None
# print(longestWord) # Neighbors


# sentence = "Hello my neighbors, nice to meet you all"

# sentenceInList = sentence.split()
# reversedList = []
# for word in reversed(sentenceInList):
#     reversedList.append(word)
# print(reversedList)


# myList = []

# myTuple = ()

# mySet = {"Mohanad", "2"}

# myDict = {"one": "1", "two": "2 "}


# classOne = {
#     "Team One": ["Ahmed", "Mohamed", "Saleh"],
#     "Team Two": ["Saeed", "Saafy", "Hesham"],
# }

# for playerOne in classOne["Team One"]:
#     for playerTwo in classOne["Team Two"]:
#         print(f"{playerOne} vs {playerTwo}")


def is_palindrome(string):
    newString = string.lower().replace(" ", "")
    print(newString[::-1] == newString)


def acronym_maker(sentence):
    acronym = str()
    senteceList = sentence.split()
    for word in senteceList:
        acronym = f"{acronym}{word[0]}"
    return acronym.upper()


# print(acronym_maker("as soon as possible"))


# def caesarCipher(string):
#     shift = 3
#     message = ""
#     for c in string:
#         if c.isalpha():
#             if c.isupper():
#                 base = ord("A")
#             else:
#                 base = ord("a")
#             position = ord(c) - base
#             newPosition = (position + shift) % 26
#             newChar = chr(newPosition + base)
#             message = f"{message}{newChar}"
#         else:
#             message = f"{message}{c}"
#     return message


# print(caesarCipher("Hello"))


# def caesarCipher(string, shift):
#     message = ""
#     for char in string:
#         if char.isspace():
#             message = f"{message} "
#         elif char.isalpha():
#             if char.isupper():
#                 base = "A"
#             else:
#                 base = "a"
#             position = ord(char) - ord(base)
#             calcPosition = ((position + shift) % 26) + ord(base)
#             newChar = chr(calcPosition)
#             message = f"{message}{newChar}"
#         else:
#             message = "Invalid Input"
#             break

#     return message


# print(caesarCipher("xyz", 3))

