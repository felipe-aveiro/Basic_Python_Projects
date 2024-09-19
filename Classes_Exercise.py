classes = {
    "Class 1": [
        {"name": "student 1", "age": 20, "id": 1},
        {"name": "student 2", "age": 21, "id": 2}
    ],
    "Class 2": [
        {"name": "student 3", "age": 22, "id": 3},
        {"name": "student 4", "age": 23, "id": 4}
    ]
}

classes["Class 2"].append({"name": "student 5", "age": 25, "id": 5})

print(f'{classes}\n')

classes["Class 1"].remove({"name": "student 1", "age": 20, "id": 1})

print(f'{classes}\n')

print(f'{classes['Class 1']}\n')

print("Class 2")
for student in classes["Class 2"]:
    print(f'Name: {student["name"]}, Age: {student["age"]}, ID: {student["id"]}')