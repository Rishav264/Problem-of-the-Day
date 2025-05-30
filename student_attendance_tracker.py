# Scenario: You're building an app to track student attendance for a course. You receive a list
# of student names who attended each day and want to compute the number of days each
# student was present.
# Problem:
# Write a method that takes multiple List<String> (one per day) and returns a Map<String
#bascially they asked for a dictonary with names of student and there attendance
# Integer> containing each student's total attendance.

database = {}

def att_tracker(input_list: list) -> dict:
    """
    Adds students to the dictionary if they are not in there. If they are
    updated their count.

    Args: input_list (list): input list from user.

    Returns: updated database (dict).
    """
    for name in input_list:
        if name in database:
            database[name] = database[name] + 1
        else:
            database[name] = 1    
    return database

print("Student Attendance Tracker:")

#taking input number of days and the attendance.
num_days = int(input("enter the num of days: "))
for i in range(num_days):
    input_list = input(f"enter the attendace of day {i+1}: ").split()
    att_tracker(input_list)

#printing each name and its value from the dictionary database.
print("The Attendance Sheet:")
for name,value in database.items():
    print(f"{name}: {value}")    
    