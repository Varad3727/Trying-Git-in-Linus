import sys

print(sys.argv)
emp_id = 10
emp_name = "Varad"
emp_sal = 20.5
print("Employee ID = ",emp_id+int(sys.argv[1]))
print("Employee Name = ",emp_name+sys.argv[2])
print("Employee salary = ",emp_sal+float(sys.argv[3]))


