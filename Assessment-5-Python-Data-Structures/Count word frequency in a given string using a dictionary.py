text = input("enter a string: ")

#split string into words
word = text.split()

#empty dictionary
frequency = {}

# count word frequency
for word in word:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:", frequency)
