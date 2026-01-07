# Student Data Management System

A Python-based system for efficiently managing, filtering, and processing student records using various data structures including lists, tuples, sets, and generators.

## 📋 Project Overview

This system demonstrates the use of different Python data structures to handle student information efficiently. It showcases:
- **Lists** for ordered, mutable collections
- **Tuples** for immutable student records
- **Sets** for tracking unique attributes
- **List/Set Comprehensions** for efficient filtering
- **Generator Expressions** for memory-efficient large dataset processing

## 🚀 Setup

### Prerequisites
- Python 3.6 or higher

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
```bash
   cd course-7-module-1-python-data-structures-lab
```

3. No additional dependencies required - uses Python standard library only!

## 📁 Project Structure
```
course-7-module-1-python-data-structures-lab/
├── lib/
│   ├── student_data.py          # Student records data
│   ├── filter.py                # Filtering functions
│   ├── data_processing.py       # Display and formatting functions
│   ├── set_operations.py        # Set-based operations
│   ├── data_generator.py        # Generator expressions
│   └── test_lab.py              # Test file for all functions
└── README.md
```

## 🎯 Features

### 1. Student Data Storage (`student_data.py`)
Stores student records as a list of tuples for efficient, immutable data representation.

**Structure:**
```python
students = [
    (ID, Name, Major),
    ...
]
```

**Example:**
```python
from lib.student_data import students
print(students[0])  # (101, 'Alice Johnson', 'Computer Science')
```

---

### 2. Filter Students by Major (`filter.py`)
Efficiently filters students by major using list comprehensions.

**Function:** `filter_students_by_major(students, major)`

**Usage:**
```python
from lib.student_data import students
from lib.filter import filter_students_by_major

cs_students = filter_students_by_major(students, "Computer Science")
print(cs_students)
# [(101, 'Alice Johnson', 'Computer Science'), (104, 'David Wilson', 'Computer Science')]
```

---

### 3. Format Student Data (`data_processing.py`)
Formats student tuples into readable strings.

**Function:** `format_student_data(student)`

**Usage:**
```python
from lib.student_data import students
from lib.data_processing import format_student_data

formatted = format_student_data(students[0])
print(formatted)
# "ID: 101 | Name: Alice Johnson | Major: Computer Science"
```

---

### 4. Display All Students (`data_processing.py`)
Displays all student records in a formatted manner.

**Function:** `display_students(students)`

**Usage:**
```python
from lib.student_data import students
from lib.data_processing import display_students

display_students(students)
```

**Output:**
```
ID: 101 | Name: Alice Johnson | Major: Computer Science
ID: 102 | Name: Bob Smith | Major: Mathematics
ID: 103 | Name: Charlie Davis | Major: Physics
ID: 104 | Name: David Wilson | Major: Computer Science
ID: 105 | Name: Eve Lewis | Major: Mathematics
```

---

### 5. Get Unique Majors (`set_operations.py`)
Returns a set of unique majors using set comprehensions.

**Function:** `unique_majors(students)`

**Usage:**
```python
from lib.student_data import students
from lib.set_operations import unique_majors

majors = unique_majors(students)
print(majors)
# {'Computer Science', 'Mathematics', 'Physics'}
```

**Key Benefit:** Automatically eliminates duplicate majors using Python sets.

---

### 6. Student Generator (`data_generator.py`)
Memory-efficient generator for filtering students - ideal for large datasets.

**Function:** `student_generator(students, major)`

**Usage:**
```python
from lib.student_data import students
from lib.data_generator import student_generator

# Create generator
math_gen = student_generator(students, "Mathematics")

# Option 1: Iterate with for loop
for student in math_gen:
    print(student)

# Option 2: Get one at a time
cs_gen = student_generator(students, "Computer Science")
print(next(cs_gen))  # First CS student
print(next(cs_gen))  # Second CS student

# Option 3: Convert to list
physics_gen = student_generator(students, "Physics")
physics_list = list(physics_gen)
```

**Key Benefit:** Only loads one student at a time into memory, perfect for processing millions of records efficiently.

---

## 🧪 Testing

Run the comprehensive test file:
```bash
cd lib
python test_lab.py
```

Or test individual functions in Python interactive shell:
```bash
cd lib
python
```
```python
>>> from student_data import students
>>> from filter import filter_students_by_major
>>> cs = filter_students_by_major(students, "Computer Science")
>>> print(cs)
>>> exit()
```

## 💡 Key Concepts Demonstrated

| Concept | Why It's Used | Example in Project |
|---------|---------------|-------------------|
| **Tuples** | Immutable data that shouldn't change | Student records (ID, Name, Major) |
| **Lists** | Ordered, mutable collections | Collection of all students |
| **Sets** | Unique values only | Tracking unique majors |
| **List Comprehensions** | Concise filtering/transformation | `filter_students_by_major()` |
| **Set Comprehensions** | Extract unique values efficiently | `unique_majors()` |
| **Generators** | Memory-efficient lazy evaluation | `student_generator()` |

## 📚 Learning Outcomes

After completing this lab, you will understand:
- ✅ When to use lists vs. tuples vs. sets
- ✅ How to write efficient comprehensions
- ✅ The difference between eager (lists) and lazy (generators) evaluation
- ✅ Memory-efficient data processing techniques
- ✅ Practical application of Python data structures

## 🤝 Contributing

This is a lab project for learning purposes. Feel free to extend it with additional features like:
- Adding/removing students
- Updating student information
- Sorting students by different criteria
- Exporting data to CSV/JSON

## 📄 License

This project is for educational purposes as part of the Flatiron School curriculum.

---

**Author:** Greg Marshall
**Date:** January 2026  
**Course:** Flatiron School - Python Data Structures