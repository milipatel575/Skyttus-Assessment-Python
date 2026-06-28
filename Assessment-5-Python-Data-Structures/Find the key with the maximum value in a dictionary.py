students = {
    "Mili": 85,
    "Diya": 92,
    "Prince": 78,
    "Chiku": 88
}

# find key with maximum value
max_key = max(students, key=students.get)

print("Student with highest marks:", max_key)
print("Marks:", students[max_key])