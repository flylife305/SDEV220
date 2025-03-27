""""
creator_name: Craig Curry
file_name: Student GPA.py
short_description: This program will accept a students last name, first name, and gpa. Then,
it will display a corresponding message dependent on the gpa value.

"""


#starts infinite loop
while True:
    #tests if user wants to enter student name or quit
    student_last_name = input("Enter student's last name or enter 'ZZZ' to quit: ")

    #condition that terminates the program
    if student_last_name == "ZZZ":
        print("Program terminated.")
        break

    #asks user for first name
    student_first_name = input("Enter student's first name: ")

    #asks user for student gpa and converts it to a float value
    student_gpa = float(input("Enter student's GPA: "))
    
    #student dean's list message
    if student_gpa >= 3.5:
        message = ("Congratulations on making the Dean's List!")
    # honor roll message
    elif student_gpa >= 3.25:
        message =("Congratulations on making the Honor Roll!")
    #default message if previous conditions are not met
    else:
        message =("Stay motivated!")

    #prints message when gpa is entered
    if student_gpa:
        print(message)


