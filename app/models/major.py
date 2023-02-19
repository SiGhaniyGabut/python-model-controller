from app.database import majors

def all():
    return majors

def find(id):
    for major in majors:
        if major['id'] == id:
            return major

def find_by(**kwargs):
    for key, value in kwargs.items():
        if key == 'id':
            return find(value)
        elif key == 'name':
            return _find_by_name(value)
        elif key == 'faculty_id':
            return _find_by_faculty_id(value)

def add(name):
    major = {
        'id': len(majors) + 1,
        'name': name,
    }

    majors.append(major)

def edit(id, name):
    major = get_by_id(id)
    if major:
        major['name'] = name

def delete(id):
    major = get_by_id(id)
    if major:
        majors.remove(major)

# PRIVATE METHODS
def _find_by_name(name):
    for major in majors:
        if major['name'] == name:
            return major

def _find_by_faculty_id(faculty_id):
    for major in majors:
        if major['faculty_id'] == faculty_id:
            return major