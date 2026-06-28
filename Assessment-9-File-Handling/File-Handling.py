# Write a program to read a file and display its contents.

file = open("demo.txt", "r")

content = file.read()
print(content)

file.close()

# Write a program to count the number of lines in a file.

file = open("demo.txt", "r")

lines = file.readlines()
count = len(lines)

print("Number of lines:", count)

file.close()


# Write a program to count how many times each word appears in a file.

file = open("demo.txt", "r")

text = file.read()
words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
file.close()

# Write a program to write 5 user-entered sentences to a file.

file = open("sentence.txt", "w")

for i in range(5):
    sentence = input("Enter Sentence: ")
    file.write(sentence + "\n")

file.close()

print("Sentence written successfully!")

# Write a program to append a list of strings to an existing file.

strings = ["\n"" Red ", " blue ", "green ", "yellow"]

file = open("demo.txt", "a")

for item in strings:
    file.write(item + "\n")

file.close()

print("Data appended successfully. ")


# Write a program to read a file and print only lines containing a specific word.

word = input("Enter word to search : ")

file = open("sentence.txt", "r")

for line in file:
    if word in line:
        print(line)
   

file.close()

# Write a program to replace a specific word in a file and save changes.

file = open("sentence.txt", "r")
text = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter a specifice new word: ")

text = text.replace(old_word, new_word)

file.close()

file = open("sentence.txt", "w")
file.write(text)

file.close()

print("word replaced successfully.")


# Write a program to merge the contents of two text files into a third file.

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

content1 = file1.read()
content2 = file2.read()

merged = open("merged.txt", "w")

merged.write(content1)
merged.write("\n")
merged.write(content2)

file1.close()
file2.close()
merged.close()

print("Files merged successfully.")


# Write a program to read a CSV file and display its content in a formatted way.

import csv

file = open("data.csv", "r")

csv_reader =  csv.reader(file)

for row in csv_reader:
    print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")

file.close()

# Write a program to back up a file by copying its contents into another file.

source = open("demo.txt", "r")

content = source.read()

backup = open("backup.txt", "w")
backup.write(content)

source.close()
backup.close()

print("backup created successfully.")