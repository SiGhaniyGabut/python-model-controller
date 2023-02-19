import app.models.faculty as Faculty
import app.models.major as Major
import app.models.student as Student

"""
Action Index acts like SELECT clause with INNER JOIN in SQL

SELECT students.id, students.name, students.year, students.grade,
majors.name AS major_name,
faculties.name AS faculty_name
FROM students
INNER JOIN majors ON majors.id = students.major_id
INNER JOIN faculties ON faculties.id = majors.faculty_id
"""
def index():
    print('ID\t | \tNama\t | \tJurusan\t\t | \tTahun\t | \tNilai')
    for student in Student.all():
        major = Major.find(student['major_id'])
        print(f"{student['id']}\t | \t{student['name']}\t | \t{major['name']}\t | \t{student['year']}\t | \t{student['grade']}")

def show():
    student_id = int(input('ID: '))
    student = Student.find(student_id)
    if student:
        major = Major.find(student['major_id'])
        faculty = Faculty.find(major['faculty_id'])
        print(f"ID: {student['id']}")
        print(f"Nama: {student['name']}")
        print(f"Fakultas: {faculty['name']}")
        print(f"Jurusan: {major['name']}")
        print(f"Tahun: {student['year']}")
        print(f"Nilai: {student['grade']}")
    else:
        print('Mahasiswa tidak ditemukan')

def add():
    name = input('Nama: ')
    year = int(input('Tahun: '))
    grade = float(input('Nilai: '))
    major_id = int(input('Jurusan ID: '))
    Student.add(name, year, grade, major_id)

def update():
    student_id = int(input('ID: '))
    student = Student.find(student_id)
    if student:
        name = input('Nama: ')
        year = int(input('Tahun: '))
        grade = float(input('Nilai: '))
        major_id = int(input('Jurusan ID: '))
        Student.update(student_id, name, year, grade, major_id)
    else:
        print('Mahasiswa tidak ditemukan')

def delete():
    student_id = int(input('ID: '))
    student = Student.find(student_id)
    if student:
        Student.delete(student_id)
    else:
        print('Mahasiswa tidak ditemukan')
