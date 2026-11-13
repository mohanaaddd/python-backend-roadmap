# Raising Exception

# x = -10
# if x < 0:
#     raise Exception(f"{x} is less than zero")
# else:
#     print(f"{x} is less than zero")
# print("this is after the if condition")


# try and catch

# try:
#     number = int(input("Enter a number : "))

# except:
#     print("This is not a number")

# else:
#     print("Good, this is integer")

# finally:
#     print("print from finally whatever happens")


# Example

# try:
#     # print(10 / 0)
#     # print(x)
#     print(int("Hello"))

# except ZeroDivisionError:
#     print("Cannot divide by 0")

# except NameError:
#     print("identfier not found")

# except:
#     print("Error Occured")


# Exceptions Handling Advanced Example

# the_file = None
# the_tries = 5

# while the_tries > 0:

#     try:  # try to open the file
#         print("Enter The File Name With Absolute Path To Open")
#         print(f"{the_tries} Tries Left")
#         print("Example: D:\\Python\\Files\\yourfile.extension")
#         file_name_and_path = input("File Name => : ").strip()

#         the_file = open(file_name_and_path, "r")

#         print(the_file.read())

#         break

#     except FileNotFoundError:
#         print("File not found, Try again...")
#         the_tries -= 1
#     except:
#         print("Error Occured")
#     finally:

#         if the_file is not None:
#             the_file.close()
#             print("File Closed")
# else:
#     print("All Tries Is Done")


# Debugging


# my_list = [1, 2, 3]

# my_dictionary = {"Name": "Osama", "Age": 36, "Country": "Egypt"}

# for num in my_list:
#     print(num)

# for key, value in my_dictionary.items():

#     print(f"{key} => {value}")


# def funciton_one_one():
#     print("Hello from function one")


# funciton_one_one()
