sentence = input("enter a string: ")
word = input("enter a word: ")

if word in sentence: 
    print(word, "is present in sentence!")
else:
    print(word, "is not present in sentence!")