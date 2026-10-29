# f = [1, 2, 3, 4, 5]

# print(f.index(5))

# f.insert(1, 10)
# f.insert(-1, True)
# f.append(False)

# print(f)

# b = f.copy()

# f.clear()

# print(f)
# print(b)

# print(b.pop(1))


# food = ["Pasta", "Rice", "Meat", "Pepperoni", "Kofta"]

# print(food[0])
# print(food[-1])
# print(len(food))


# print(food[1:4])
# reversed_food = food[::-1]
# print(reversed_food) # ['Kofta', 'Pepperoni', 'Meat', 'Rice', 'Pasta']
# print(reversed_food[0:2])
# print(reversed_food[-2:])

# food.append("Cheese")
# food.insert(0, "Hamburger")
# food.remove("Rice")
# print(food)
# food.pop()
# print(food)
# food.sort()
# print(food)

# my guess: 40
# print([10, 20, 30, 40, 50][-2])
# my guess: 20,30,40
# print([10, 20, 30, 40, 50][1:4])


# birth_date = (2005, 1, 1)
# print(birth_date[0])
# print(birth_date[1])
# print(birth_date[2])
# birth_date[0] = 2004 // Error Tuples can't add or delete


# myList = [38, 13, 15, 86, 23, 78]

# for num in myList:
#     print(num * 2)

# for num in myList:
#     if num % 2 == 0:
#         print(num)


############################### THE TO-DO LIST#########################################

app_opened = True
myTasks = []
while app_opened == True:
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    user_input = int(input("Enter a number : "))
    if user_input == 1:
        if len(myTasks) == 0:
            print("No Tasks Yet")
        else:
            number = 1
            for task in myTasks:
                print(f"{number} - {task}")
                number = number + 1

    elif user_input == 2:
        newTask = str(input("Enter your task : "))
        myTasks.append(newTask)

    elif user_input == 3:
        removeTask = int(input("Enter your task number to remove : "))
        if removeTask <= len(myTasks):
            real_del_val = removeTask - 1
            if 0 <= real_del_val <= 100:
                myTasks.pop(real_del_val)
                print(f"Task {removeTask} is removed successfully")
            else:
                print("Task was not found")
        else:
            print("Task was not found")

    elif user_input == 4:
        app_opened = False

    else:
        print("Please enter a number from 1 --> 4")
