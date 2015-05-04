from the_last_hr import GatherInfo
import sqlite3


hackbg_info = GatherInfo("https://hackbulgaria.com/api/students/")
db = sqlite3.connect("students_data.db")
cursor = db.cursor()

# Create tables
create_students_table = """
CREATE TABLE IF NOT EXISTS
Students(student_id INTEGER PRIMARY KEY, student_name TEXT, student_github TEXT)
"""
cursor.execute(create_students_table)

create_courses_table = """
CREATE TABLE IF NOT EXISTS
Courses(course_id INTEGER PRIMARY KEY, course_name TEXT)
"""
cursor.execute(create_courses_table)

create_students_to_courses_table = """
CREATE TABLE IF NOT EXISTS
Students_to_courses(s_id INTEGER, c_id INTEGER,
FOREIGN KEY (s_id) REFERENCES Students(id),
FOREIGN KEY (c_id) REFERENCES Courses(id))
"""
cursor.execute(create_students_to_courses_table)
db.commit()

# Insert students
cursor.executemany(""" INSERT INTO Students(
student_name,
student_github) VALUES(?,?)""", hackbg_info.get_student_and_github())
db.commit()

# Insert courses
cursor.executemany(""" INSERT INTO Courses(
course_name) VALUES(?)""", hackbg_info.get_all_courses())
db.commit()

# Create students and courses dicts
courses_ids_names = cursor.execute(
    "SELECT course_id, course_name FROM Courses")
courses_dict = {course[1]: course[0] for course in courses_ids_names}
db.commit()

students_ids_names = cursor.execute(
    "SELECT student_id, student_name FROM Students")
students_dict = {student[1]: student[0] for student in students_ids_names}
db.commit()

# Insert relations
for student_and_course in hackbg_info.get_student_and_course():
    for course in student_and_course[1]:
        cursor.execute(""" INSERT INTO Students_to_courses(
s_id, c_id) VALUES(?,?)""", (students_dict[student_and_course[0]], courses_dict[course]))
db.commit()
