# This module contains functions to process student data.

def format_student_data(student):
    """
    Formats a student tuple into a readable string.
    
    Args:
        student: Tuple containing (ID, Name, Major)
    
    Returns:
        Formatted string: "ID: X | Name: Y | Major: Z"
    """
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"
    pass

def display_students(student_list):
    """
    Displays all student records in a formatted way.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        None (prints to console)
    """
    for student in students:
        print(format_student_data(student))
    pass