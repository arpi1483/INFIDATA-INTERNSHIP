student = {
    "Name": "Arun",
    "Id": 101,
    "Branch": 'CS',
    "Age": 20,
    "Gender": 'male',
    "City": 'Bangalore'
}
print("Before Delete :", student)
# Keys to remove From a Dict
keys = ["Id", "City"]

for k in keys:
    student.pop(k)
print("After Delete :", student)

