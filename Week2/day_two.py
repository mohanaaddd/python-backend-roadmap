# =======Sets=======
# can't be sliced
# can't be indexed
# not ordered
# only Immutable data types (not changeable)
# like strings number, tuples. can't for lists and dicts
# set items is unique, will work but only use one

# mySetOne = {100, "Osama", "Ahmed"}
# mySetTwo = {100, "Jomana", "Mai"}
# mySetThree = {100, "Haidy", "Nour"}

# mySetOne.clear()
# print(mySetOne)

# print(mySetOne.union(mySetTwo))
# d = {1, 2, 3, 4}

# d.add(5)
# d.add(6)
# print(d)

# e = {1, 2, 3, 4}

# f = e.copy()

# print(e)
# print(f)

# e.add(6)

# print(e)
# print(f)

# remove with erorrs
# g = {1, 2, 3, 4}
# g.remove(1)
# print(g)


# remove without erorrs
# h = {1, 2, 3, 4}

# h.discard(6)
# print(h)


# i = {1, 2, 3, 4}

# print(i.pop())


# j = {1, 2, 3}
# k = {1, "A", "B", 2}
# j.update(["Html", "CSS"])
# j.update(k)
# print(j)


# a = {1, 2, 3, 4}
# b = {1, 2, 3, "Osama", "Ahmed"}

# print(a)
# print(a.difference(b))
# print(a)

# a = {1, 2, 3, 4}
# b = {1, 2, 3, "Osama", "Ahmed"}

# a.difference_update(b)
# print(a)


# a = {1, 2, 3, 4, "X"}
# b = {"osama", "X", 2}
# print(a)
# print(a.intersection(b))
# print(a)

# a = {1, 2, 3, 4, "X", "osama"}
# b = {"osama", "X", 2}
# a.intersection_update(b)
# print(a)

# a = {1, 2, 3, 4, 5, "X"}
# b = {"Osama", "Zero", 1, 2, 3, 4}
# a.symmetric_difference_update(b)
# print(a)


# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# c = {10, 11, 12}

# print(a.issuperset(b))
# print(a.issuperset(c))

# print(a.issubset(b))
# print(a.issubset(c))

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))


# =======Dictionarys=======
# Dict items are enclosed in curly brackets {}
# Dict items are in key:value pairs
# Dict keys have to be immutable (string, number, tuple)
# Dict values can be any data type and can be duplicated
# Dict keys have to be unique
# DIct is not ordered, access by key not by index

# user = {
#     "name": "Osama",
#     "age": 36,
#     "Country": "Egypt",
#     "skills": ["Html", "CSS", "JS"],
#     "rating": 10.5,
#     "name": "Ahmed",  # the updated value will be used because the key is the same
# }

# print(user.get("rating"))
# print(user["rating"])
# print(user.keys())
# print(user.values())

# languages = {
#     "One": {
#         "name": "Html",
#         "progress": "80%",
#     },
#     "Two": {
#         "name": "CSS",
#         "progress": "90%",
#     },
#     "Three": {
#         "name": "JS",
#         "progress": "50%",
#     },
# }
# print(languages.get("One").get("name"))

# print(languages["Three"]["progress"])
# print(len(languages))
# print(len(languages["One"]))


# frameworkOne = {
#     "name": "Vuejs",
#     "progress": "80%",
# }

# frameworkTwo = {
#     "name": "Reactjs",
#     "progress": "90%",
# }

# frameworkThree = {
#     "name": "Angular",
#     "progress": "50%",
# }

# frameworkFour = {"name": "React.js", "progress": "0%"}

# allFrameworks = {
#     "One": frameworkOne,
#     "Two": frameworkTwo,
#     "Three": frameworkThree,
#     "Four": frameworkFour,
# }

# print(allFrameworks["Four"]["name"])

# Dictionary Methods
# user = {
#     "name": "Osama",
# }

# print(user)
# user.clear()
# print(user)

# print("=" * 50)

# member = {"name": "Osama"}
# print(member)
# member["age"] = 36
# print(member)
# member.update({"Country": "Egypt"})
# print(member)

# print("=" * 50)

# main = {"name": "Osama"}

# b = main.copy()

# print(b)
# main.update({"skill": "Fighting"})
# print(b)
# print(main)

# print(main.keys())
# print(main.values())


# user = {"name" : "Osama"}
# print(user)
# print(user.setdefault("age"))
# print(user)

# print("=" * 50)

# member = {"name": "Osama", "skills": "PS4"}

# print(member)

# member.update({"age": 36})
# print(member.popitem())


# view = {"name": "Osama", "skill": "Xbox"}

# allItems = view.items()
# print(view)
# print(allItems)

# view["age"] = 36

# print(allItems)


# a = (1, 2, 3)
# b = "X"
# c = "Y"
# print(dict.fromkeys(a, b))

# list = [1, 2, 3]
# tuple = (1, 2, 3)
# set = {1, 2, 3}
# dicte = {"num1": 1, "num2": 2, "num3": 3}

# print(list)
# print(tuple)
# print(set)
# print(dicte)

# list.append(2)
# print(list)
# set.add(4)
# print(set)
# dicte["num4"] = 4
# print(dicte)


# ====================Word Counter====================

# sentence = input("Enter a sentence: ")  # the cat and the dog and the bird

# for mark in ",.!?;:":
#     sentence = sentence.replace(mark, "")
# splitted_sentence = sentence.lower().split()
# words = {}

# for word in splitted_sentence:
#     if word in words:
#         words[word] += 1
#     else:
#         words[word] = 1


# def get_count(pair):
#     return pair[1]


# words_list = list(words.items())
# ranked_words_all = sorted(words_list, key=get_count, reverse=True)
# ranked_words_top3 = ranked_words_all[:3]

# for word_top3, count in ranked_words_top3:
#     print(f"{word_top3} : {count}")


# myDict = ["Ahmed", "Ali", "Sara", "Salma", "Omar"]
# newDict = {}
# for key, value in myDict.items():
#     newDict[value] = key
# print(newDict)


# a = {"x": 1, "y": 2}
# b = {"y": 20, "z": 3}
# c = a.copy()
# c.update(b)
# print(c)

## grouping names with first letter

# names = ["Ahmed", "Sara", "Ali"]
# charDict = {}

# for name in names:
#     if name[0] in charDict:
#         charDict[name[0]].append(name)
#     else:
#         charDict[name[0]] = [name]
# print(charDict)


# finding duplicates in a list

mySet = [1, 2, 3, 4, 5, 2, 3, 4]

seen = list()
duplicates = list()

for item in mySet:
    if item in seen:
        duplicates.append(item)
    else:
        seen.append(item)

print(f"Duplicates: {duplicates}")
