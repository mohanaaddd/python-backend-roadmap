# def hello_python():
#     print("Hello Python")

# hello_python()


# def hello_python():
#     return "Hello Python"


# print(hello_python())
# dataFromFunction = hello_python()
# print(dataFromFunction)


# a, b, c = "Ahmed", "Osama", "Samir"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")


# def say_hello(name):
#     print(f"Hello {name}")


# say_hello("Ahmed")
# say_hello(a)
# say_hello(b)
# say_hello(c)


# def addition(n1, n2):

#     if type(n1) != int or type(n2) != int:

#         print("Only integers Allowed")

#     else:

#         print(n1 + n2)


# addition(100, 300)


# def full_name(first, middle, last):
#     print(
#         f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()} "
#     )


# full_name("Mohanad", "Ahmed", "mohamed")


## default parameter
# def say_hello(name="Unknown", age="Unknown", country="Unknown"):
#     print(
#         f"Hello {name.capitalize()}, Your age is {age}, and your country is {country.capitalize()}"
#     )


# say_hello("osama", 36, "egypt")
# say_hello("Ahmed", 22)
# say_hello(country="Egypt")


# def one():
#     global x
#     x = 2
#     print(f"Fun-one x = {x}")


# def two():
#     x = 10
#     print(f"Fun-two x = {x}")


# one()
# two()
# print(x)


# ========================================================================Coding Session========================================================================

## Grade calculator for logic operations (Remake with Funcitons)
# student_name = str(input("What is your name? : "))
# grade_maths1 = float(input(f"Enter your grade in Maths 1 : "))
# grade_maths2 = float(input(f"Enter your grade in Maths 2 : "))
# grade_maths3 = float(input(f"Enter your grade in Maths 3 : "))


# def get_grade(name, math1, math2, math3):
#     grade_letter = ""
#     average = (math1 + math2 + math3) / 3

#     if average == 100:
#         grade_letter = "Perfect"

#     elif average >= 90:
#         grade_letter = "A"

#     elif average >= 80:
#         grade_letter = "B"

#     elif average >= 70:
#         grade_letter = "C"

#     elif average >= 60:
#         grade_letter = "D"
#     else:
#         grade_letter = "E"

#     if (math1 < 50) or (math2 < 50) or (math3 < 50):
#         result = "Failed"
#     else:
#         result = "Passed"

#     if (average >= 90) and (result == "Passed"):
#         honors = "Yes"
#     else:
#         honors = "No"

#     print(f"Student : {name}")
#     print(f"Average : {average:.1f}")
#     print(f"Grade : {grade_letter}")
#     print(f"Result : {result}")
#     print(f"Honors : {honors}")


# if not (
#     0 <= grade_maths1 <= 100 and 0 <= grade_maths2 <= 100 and 0 <= grade_maths3 <= 100
# ):
#     print("Invalid inputs, grades must be from 0 to 100.")

# else:
#     get_grade(
#         name=student_name, math1=grade_maths1, math2=grade_maths2, math3=grade_maths3
#     )


# THEE FIZZZBUZZZZZZ (Remake with Functions)
# def fizzbuzz(x):
#     return x % 3 == 0 and x % 5 == 0


# def fizzbuzzzzzzzzz():
#     for x in range(1, 101):
#         if fizzbuzz(x=x) is True:
#             print("FizzBuzz")
#         elif x % 5 == 0:
#             print("Buzz")
#         elif x % 3 == 0:
#             print("Fizz")
#         else:
#             print(x)


# fizzbuzzzzzzzzz()


############################### THE TO-DO LIST#########################################

# app_opened = True
# myTasks = []


# def user_input_function():
#     global user_input
#     user_input = int(input("Enter a number : "))
#     return user_input


# def showTasks():
#     if len(myTasks) == 0:
#         print("No Tasks Yet")
#     else:
#         number = 1
#         for task in myTasks:
#             print(f"{number} - {task}")
#             number = number + 1


# def addTask():
#     newTask = str(input("Enter your task : "))
#     myTasks.append(newTask)


# def removeTask():
#     removeTask = int(input("Enter your task number to remove : "))
#     if removeTask <= len(myTasks):
#         real_del_val = removeTask - 1
#         if 0 <= real_del_val <= 100:
#             myTasks.pop(real_del_val)
#             print(f"Task {removeTask} is removed successfully")
#         else:
#             print("Task was not found")
#     else:
#         print("Task was not found")


# while app_opened == True:
#     print("1. Show tasks")
#     print("2. Add task")
#     print("3. Remove task")
#     print("4. Quit")
#     user_input_function()

#     if user_input == 1:
#         showTasks()

#     elif user_input == 2:
#         addTask()

#     elif user_input == 3:
#         removeTask()

#     elif user_input == 4:
#         app_opened = False

#     else:
#         print("Please enter a number from 1 --> 4")


# DRILLS


# def is_even(x):
#     if x % 2 == 0:
#         return print(True)
#     else:
#         return print(False)


# is_even(14)


# def max_of_3(x, y, z):
#     myList = [x, y, z]
#     myList.sort()
#     return print(myList.pop())


# max_of_3(9000, 900, 90)


# def factorial(x):
#     i = 1
#     result = 1
#     while i <= x:
#         result *= i
#         i += 1
#     return result


# print(factorial(3))


# def reverseString(x):
#     text = x[::-1]
#     return print(text)

# reverseString("Hello")


# def countVowels(word):
#     count = 0
#     for char in word:
#         if char.lower() in "aeiou":
#             count += 1
#     return print(count)


# countVowels("OAIE")


# def celsToFahren(x):
#     y = x * 9 / 5 + 32

#     return print(f"{y}°F")

# celsToFahren(3)

# reverseString("Hello")


# def reverseString(x):
#     text = x[::-1]
#     return text


# def is_palindrome(x):
#     reversed = reverseString(x.lower())
#     print(x.lower() == reversed)


# is_palindrome("Racecar")


def avg_list(myList):
    return int(sum(myList) / len(myList))


myList = [5, 5, 10, 20]
print(avg_list(myList))
