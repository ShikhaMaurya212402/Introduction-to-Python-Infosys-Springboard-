attendance = [
    ("Ajay", "2026-01-01", "Present"),
    ("Ajay", "2026-01-02", "Absent"),
    ("Rahul", "2026-01-01", "Present")
]

def attendance_percentage(attendance):
    total_days = {}
    present_days = {}

    for record in attendance:
        name = record[0]
        status = record[2]

        if name not in total_days:
            total_days[name] = 0
            present_days[name] = 0

        total_days[name] += 1

        if status == "Present":
            present_days[name] += 1

    percentage = {}
    for name in total_days:
        percentage[name] = (present_days[name] * 100) / total_days[name]

    return percentage

def low_attendance_students(percentages):
    low_attendance = []

    for name in percentages:
        if percentages[name] < 75:
            low_attendance.append(name)

    return low_attendance

def longest_present_streak(attendance):
    current_streak = {}
    max_streak = {}

    for record in attendance:
        name = record[0]
        status = record[2]

        if name not in current_streak:
            current_streak[name] = 0
            max_streak[name] = 0

        if status == "Present":
            current_streak[name] += 1
            if current_streak[name] > max_streak[name]:
                max_streak[name] = current_streak[name]
        else:
            current_streak[name] = 0

    return max_streak

percentages = attendance_percentage(attendance)
low_attendance = low_attendance_students(percentages)
streaks = longest_present_streak(attendance)

print("Attendance Percentage:", percentages)
print("Students with attendance < 75%:", low_attendance)
print("Longest Present Streak:", streaks)
