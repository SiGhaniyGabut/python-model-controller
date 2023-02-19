from app.database import students

def all():
    return students

def find(id):
    for student in students:
        if student['id'] == id:
            return student

def find_by(**kwargs):
    for key, value in kwargs.items():
        if key == 'id':
            return find(value)
        elif key == 'name':
            return _find_by_name(value)
        elif key == 'year':
            return _find_by_year(value)
        elif key == 'grade':
            return _find_by_grade(value)
        elif key == 'major_id':
            return _find_by_major_id(value)

def add(name, year, grade, major_id):
    student = {
        'id': len(students) + 1,
        'name': name,
        'year': year,
        'grade': grade,
        'major_id': major_id,
    }

    students.append(student)

def update(id, name, year, grade, major_id):
    student = get_by_id(id)
    if student:
        student['name'] = name
        student['year'] = year
        student['grade'] = grade
        student['major_id'] = major_id

def delete(id):
    student = get_by_id(id)
    if student:
        students.remove(student)

# PRIVATE METHODS
def _find_by_id(id):
    for student in students:
        if student['id'] == id:
            return student

def _find_by_name(name):
    for student in students:
        if student['name'] == name:
            return student

def _find_by_year(year):
    for student in students:
        if student['year'] == year:
            return student

def _find_by_grade(grade):
    for student in students:
        if student['grade'] == grade:
            return student

def _find_by_major_id(major_id):
    for student in students:
        if student['major_id'] == major_id:
            return student