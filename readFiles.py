employee_file = open("employees.txt", "r")

print(employee_file.readable())

print(employee_file.read())

for employee in employee_file.readlines():
    print(employee)

# print(employee_file.readline())
# print(employee_file.readline())

print(employee_file.readlines()) # list of lines


employee_file.close()
# open(employees.txt, "a")
# open(employees.txt, "r+")
# open(employees.txt, "w")