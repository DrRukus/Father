#!/usr/bin/env python

student = {
    'name': 'Jose',
    'marks': [70, 80, 91, 78, 48],
    'exams': {
        'final': 90,
        'midterm': 50
    }
}

def create_student():
    # Ask the user for the student's name
    # Create the dictionary in the format
    # {'name': '<student_name>', 'marks': []}
    # Return that dictionary
    name = input('Name: ')
    return {'name': name, 'marks': []}

print(create_student())
