import psycopg2

DB_CONFIG = {
    "dbname": "eschool_db",
    "user": "postgres",
    "password": "09890",
    "host": "localhost",
    "port": "5432"
}

def connect_db():
    """Создаёт и возвращает соединение с БД"""
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    """Создаёт таблицы, если их нет"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("""
            CREATE TABLE IF NOT EXISTS courses(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) UNIQUE,
                description TEXT
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXISTS teachers(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXISTS enrollments(
                id SERIAL PRIMARY KEY,
                student_id INT REFERENCES students(id) ON DELETE CASCADE,
                course_id INT REFERENCES courses(id) ON DELETE CASCADE,
                grade INT CHECK (grade BETWEEN 0 AND 100)
            );
        """)

        conn.commit()

# --- Функции для работы с БД ---

def add_course(name, description):
    """Добавляет курс"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("INSERT INTO courses (name, description) VALUES (%s, %s) RETURNING id;", (name, description))
        conn.commit()
        return curr.fetchone()[0]

def add_teacher(name, email):
    """Добавляет преподавателя"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("INSERT INTO teachers (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
        conn.commit()
        return curr.fetchone()[0]

def add_student(name, email):
    """Добавляет студента"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("INSERT INTO students (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
        conn.commit()
        return curr.fetchone()[0]

def enroll_student(student_id, course_id, grade=None):
    """Записывает студента на курс"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("INSERT INTO enrollments (student_id, course_id, grade) VALUES (%s, %s, %s);",
                     (student_id, course_id, grade))
        conn.commit()

def get_student_progress(student_id):
    """Получает успеваемость студента"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("""
            SELECT c.name, e.grade 
            FROM enrollments e
            JOIN courses c ON e.course_id = c.id
            WHERE e.student_id = %s;
        """, (student_id,))
        return curr.fetchall()

def search_course_by_name(name):
    """Ищет курс по имени"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("SELECT id, name, description FROM courses WHERE name ILIKE %s;", (f"%{name}%",))
        return curr.fetchall()