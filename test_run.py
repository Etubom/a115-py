emp_dict = {"Name": "Pankaj", "ID": 1}

try:
    emp_id = emp_dict["ID"]
    print(emp_id)

    emp_role = emp_dict["Role"]
    print(emp_role)
except KeyError as ke:
    print("Key Not Found in Employee Dictionary:", ke)
