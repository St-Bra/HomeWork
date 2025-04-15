from flask import Flask, jsonify, request
from db import (add_course, get_all_courses, edit_course, del_course,
                add_teacher, get_all_teachers, edit_teacher, del_teacher,
                add_student, get_all_students, edit_student, del_student,
                enroll_student, get_student_progress, search_course_by_name)
import http

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify('')

@app.route('/menu', methods=['GET'])
def print_menu():
    menu = {
        "0": "Выход",
        "1": "Действия с курсом",
        "2": "Действия с преподавателем",
        "3": "Действия с студентом",
        "4": "Поставить оценку студенту",
        "5": "Посмотреть прогресс студента",
        "6": "Найти курс по названию"
    }
    return jsonify(menu)

# --- Маршруты для курсов ---
@app.route('/courses', methods=['GET'])
def all_courses():
    posts = get_all_courses()
    return jsonify({'posts': posts}), http.HTTPStatus.OK

@app.route('/courses', methods=['POST'])
def add_new_course():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
    except Exception as e:
        return jsonify({'error': f'{e}'}), http.HTTPStatus.BAD_REQUEST

    add_course(name, description)
    return jsonify({'message': 'New course added successfully'}), http.HTTPStatus.OK

@app.route('/courses/<int:course_id>', methods=['DELETE'])
def del_courses(course_id):
    if course_id is None or course_id <= 0:
        return jsonify({'error': 'Invalid course id'}), http.HTTPStatus.BAD_REQUEST

    del_course(course_id)
    return jsonify({'message': 'Course deleted successfully'}), http.HTTPStatus.OK

@app.route('/courses/<int:course_id>', methods=['PATCH'])
def update_course(course_id):
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
    except Exception as e:
        return jsonify({'error': f'{e}'}), http.HTTPStatus.BAD_REQUEST

    edit_course(course_id, name, description)
    return jsonify({'message': 'Course updated successfully'}), http.HTTPStatus.OK

# --- Маршруты для преподавателей ---
@app.route('/teachers', methods=['GET'])
def all_teachers():
    teachers = get_all_teachers()
    return jsonify({'teachers': teachers}), http.HTTPStatus.OK

@app.route('/teachers', methods=['POST'])
def add_new_teacher():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
    except Exception as e:
        return jsonify({'error': f'{e}'}), http.HTTPStatus.BAD_REQUEST

    add_teacher(name, email)
    return jsonify({'message': 'New teacher added successfully'}), http.HTTPStatus.OK

@app.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def del_teacher_by_id(teacher_id):
    if teacher_id is None or teacher_id <= 0:
        return jsonify({'error': 'Invalid teacher id'}), http.HTTPStatus.BAD_REQUEST

    del_teacher(teacher_id)
    return jsonify({'message': 'Teacher deleted successfully'}), http.HTTPStatus.OK

@app.route('/teachers/<int:teacher_id>', methods=['PATCH'])
def update_teacher(teacher_id):
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
    except Exception as e:
        return jsonify({'error': f'{e}'}), http.HTTPStatus.BAD_REQUEST

    edit_teacher(teacher_id, name, email)
    return jsonify({'message': 'Teacher updated successfully'}), http.HTTPStatus.OK

# --- Маршруты для студентов ---
@app.route('/students', methods=['GET'])
def all_students():
    students = get_all_students()
    return jsonify({'students': students}), http.HTTPStatus.OK

@app.route('/students', methods=['POST'])
def add_new_student():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
    except Exception as e:
        return jsonify({'error': f'{e}'}), http.HTTPStatus.BAD_REQUEST

    add_student(name, email)
    return jsonify({'message': 'New student added successfully'}), http.HTTPStatus.OK

@app.route('/students/<int:student_id>', methods=['DELETE'])
def del_student_by_id(student_id):
    if student_id is None or student_id <= 0:
        return jsonify({'error': 'Invalid student id'}), http.HTTPStatus.BAD_REQUEST

    del_student(student_id)
    return jsonify({'message': 'Student deleted successfully'}), http.HTTPStatus.OK

@app.route('/students/<int:student_id>', methods=['PATCH'])
def update_student(student_id):
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
    except Exception as e:
        return jsonify({'error': f'{e}'}), http.HTTPStatus.BAD_REQUEST

    edit_student(student_id, name, email)
    return jsonify({'message': 'Student updated successfully'}), http.HTTPStatus.OK

@app.route('/enroll_students/<int:student_id>', methods=['POST'])
def enroll_students(student_id):
    try:
        data = request.get_json()
        course_id = data.get('course_id')
        grade = data.get('grade')
    except Exception as e:
        return jsonify({'error': f'{e}'}), http.HTTPStatus.BAD_REQUEST

    enroll_student(student_id, course_id, grade)
    return jsonify({'message': 'Student received a grade'}), http.HTTPStatus.CREATED

@app.route('/student_progress/<int:student_id>', methods=['GET'])
def student_progress(student_id):
    if student_id is None or student_id <= 0:
        return jsonify({'error': 'Invalid student id'}), http.HTTPStatus.BAD_REQUEST
    progress = get_student_progress(student_id)
    return jsonify({"studets progress": progress}), http.HTTPStatus.OK

@app.route('/search_course', methods=['GET'])
def search_course():
    try:
        data = request.get_json()
        name = data.get('name')
        if not name:
            return jsonify({'error': 'Name parameter is required'}), http.HTTPStatus.BAD_REQUEST

        courses = search_course_by_name(name)

        if courses:
            return jsonify({'courses': courses}), http.HTTPStatus.OK
        else:
            return jsonify({'message': 'No courses found'}), http.HTTPStatus.OK
    except Exception as e:
        return jsonify({'error': f'{e}'}), http.HTTPStatus.INTERNAL_SERVER_ERROR

app.run()
