employees = [
    {"name": "Ajay", "age": 22, "salary": 25000},
    {"name": "Rahul", "age": 25, "salary": 40000},
    {"name": "Kiran", "age": 21, "salary": 30000}
]

def sort_by_salary_desc(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]["salary"] < data[j + 1]["salary"]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def sort_by_age_then_salary(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (data[j]["age"] > data[j + 1]["age"]) or \
               (data[j]["age"] == data[j + 1]["age"] and 
                data[j]["salary"] > data[j + 1]["salary"]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def custom_sort(data, keys):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            for key in keys:
                if data[j][key] > data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    break
                elif data[j][key] < data[j + 1][key]:
                    break
    return data

# Salary descending
print("Sorting by Salary Descending:\n")
print(sort_by_salary_desc(employees.copy()))

# Age then salary
print("\nSorting by Age then Salary:\n")
print(sort_by_age_then_salary(employees.copy()))

# Dynamic sort (age → salary)
print("\nCustom Sorting by Age then Salary:\n")
print(custom_sort(employees.copy(), ["age", "salary"]))

# Dynamic sort (name)
print("\nCustom Sorting by Name:\n")
print(custom_sort(employees.copy(), ["name"]))
