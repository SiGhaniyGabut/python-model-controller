from app.database import faculties

def all():
    return faculties

def find(id):
    for faculty in faculties:
        if faculty['id'] == id:
            return faculty

def find_by(**kwargs):
    for key, value in kwargs.items():
        if key == 'id':
            return find(value)
        elif key == 'name':
            return _find_by_name(value)

def add(name):
    faculty = {
        'id': len(faculties) + 1,
        'name': name,
    }

    faculties.append(faculty)

def edit(id, name):
    faculty = get_by_id(id)
    if faculty:
        faculty['name'] = name

def delete(id):
    faculty = get_by_id(id)
    if faculty:
        faculties.remove(faculty)

# PRIVATE METHODS
def _find_by_name(name):
    for faculty in faculties:
        if faculty['name'] == name:
            return faculty