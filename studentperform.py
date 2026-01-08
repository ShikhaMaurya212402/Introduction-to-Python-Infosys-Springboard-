def student_performance(students):
    result = {}
    topper_name = None
    topper_avg = 0

    for name, marks in students:
        average = round(sum(marks) / len(marks), 2)

        # Classification
        if average >= 85:
            status = "Distinction"
        elif average >= 50:
            status = "Pass"
        else:
            status = "Fail"

        result[name] = {
            "average": average,
            "status": status
        }

        # Find topper
        if average > topper_avg:
            topper_avg = average
            topper_name = name

    return result, topper_name
students = [
    ("Ajay", [78, 85, 90]),
    ("Kumar", [65, 70, 60]),
    ("Rahul", [88, 92, 95])
]

performance, topper = student_performance(students)

print("Student Performance:", performance)
print("Topper:", topper)
