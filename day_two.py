# if & elif & else statements

# user_name = "Mohanad"
# course_name = "Python Programming"
# course_price = 100
# course_discount = 20
# input_country = input("Please enter your country: ")

# if input_country == "Egypt":
#     course_discount = 80
# elif input_country == "USA":
#     course_discount = 50
# else:
#     course_discount = course_discount

# print(f"Hello {user_name}, welcome to \"{course_name}\", because you are from {input_country}, the final price is: {course_price - course_discount}$")

## boolean logic operators

# age = 21
# name = "Mohanad"
# print(age.is_integer())

# print(age == 21 and name == "Mostafa")
# print(age == 21 and name == "Mohanad")

# print(age == 21 or name == "Mostafa")

# print(name is "Mohanad")
# print(name is not "Mohanad")


# print (age > 20)
# print (not not not not not age > 20)
# print (age != 20)
# print (age != 21)


## Grade calculator

grade = float(input("What is your grade? : "))
grade_letter = "A"
pass_or_fail = True

if grade < 0 or grade > 100:

    print(
        "Something is not right, please make sure you entered a correct score (0-100)."
    )
    
else :

    if grade == 100:
        grade_letter = "Perfect"

    elif grade >= 90:
        grade_letter = "A"

    elif grade >= 80:
        grade_letter = "B"

    elif grade >= 70:
        grade_letter = "C"

    elif grade < 70:
        grade_letter = "F"
        pass_or_fail = False

    if grade <= 100 and grade >= 70:
        if pass_or_fail == True:
            print(f"Congrats you got an {grade_letter}!")

    else:
        print(f"Sorry to inform, you got {grade_letter}!")