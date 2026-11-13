line_count = 0
# count the lines

# with open("Week2/notes.txt", "r") as f:
#     for eachLine in f:
#         line_count += 1
#     print(f"Lines: {line_count}")

# count the words

# with open("Week2/notes.txt", "r") as f:
#     wordsCounter = 0
#     for eachLine in f:
#         wordsCounter += len(eachLine.split())
#     print(wordsCounter)

# search

# keyWord = str(input("Enter a keyword to search for : "))

# with open("Week2/notes.txt", "r") as f:
#     found = False
#     foundLine = ""

#     for Line in f:
#         if keyWord in Line:
#             print(Line.strip())
#             found = True
#     if not found:
#         print("Not Found")
