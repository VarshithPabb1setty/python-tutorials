# employee_file = open("employees.txt", "a") # append as last line of file

# employee_file = open("employees.txt", "w") # overwrite existing file

employee_file = open("employees1.txt", "w") # overwrite existing file


print(employee_file.write("\nToby - Python"))

employee_file.close()