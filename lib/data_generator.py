# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Returns a generator expression for students filtered by major.
    Memory-efficient for large datasets.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        major: String representing the major to filter by
    
    Returns:
        Generator expression yielding matching students
    """
    return (student for student in students if student[2] == major)
    pass
