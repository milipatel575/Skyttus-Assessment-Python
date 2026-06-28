students = {
    "Mili": 85,
    "Diya": 92,
    "Prince": 78,
    "Chiku": 88
}

# reverse keys and values 

reverse_dict = {}
for key, value in students.items():
   reverse_dict[value] = key

print("Reversed dictionary:", reverse_dict)
