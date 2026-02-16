def get_student():
    student1 = {
        "name": "Rakib",
        "age": 21,
        "city": "Dhaka"
    }
    student2 = {
        "name": "Rakib2",
        "age": 21,
        "city": "Dhaka2"
    }
    return (student1,student2)

x, y = get_student()
l = list(get_student())
print(l)
