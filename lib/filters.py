# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Filters students by major using list comprehension.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        major: String representing the major to filter by
    
    Returns:
        List of student tuples matching the given major
    """
    return [student for student in students if student[2] == major]

pass