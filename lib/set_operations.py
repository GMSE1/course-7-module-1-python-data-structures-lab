# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Returns a set of unique majors from the student list.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        Set of unique major strings
    """
    return {student[2] for student in students}
    pass
