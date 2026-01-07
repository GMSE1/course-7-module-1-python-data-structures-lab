# Import your functions
from student_data import students
from filter import filter_students_by_major
from data_processing import format_student_data, display_students
from set_operations import unique_majors
from data_generator import student_generator

print("=" * 50)
print("TESTING STEP 1: Student Data")
print("=" * 50)
print(f"Total students: {len(students)}")
print(f"First student: {students[0]}\n")

print("=" * 50)
print("TESTING STEP 2: Filter by Major")
print("=" * 50)
cs_students = filter_students_by_major(students, "Computer Science")
print(f"Computer Science students: {cs_students}\n")

print("=" * 50)
print("TESTING STEP 3: Format Student Data")
print("=" * 50)
print(format_student_data(students[0]))
print()

print("=" * 50)
print("TESTING STEP 4: Display All Students")
print("=" * 50)
display_students(students)
print()

print("=" * 50)
print("TESTING STEP 5: Unique Majors")
print("=" * 50)
majors = unique_majors(students)
print(f"Unique majors: {majors}\n")

print("=" * 50)
print("TESTING STEP 6: Generator Expression")
print("=" * 50)
math_gen = student_generator(students, "Mathematics")
print("Mathematics students (using generator):")
for student in math_gen:
    print(f"  {student}")