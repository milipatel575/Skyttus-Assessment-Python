students = {
    "Mili": 85,
    "Diya": 90,
    "Prince" : 78
}

# check key 
key = input("enter student name: ")
if key in students:
    print("Key exists in dictionary")
else: 
    print("key does not exists in dictionary")