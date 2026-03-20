import sqlite3

conn = sqlite3.connect("students.db")

def create_table_students(conn: sqlite3.Connection):
    cur = conn.cursor()

    cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
    conn.commit()

def create_table_courses(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE
        );
    """)
    conn.commit()

def create_table_enrollments(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            PRIMARY KEY (student_id, course_id),
            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
        );
    """)
    conn.commit()

def add_new_student(conn: sqlite3.Connection, name: str, email: str):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students(name, email) VALUES (?, ?);",
        (name, email)
    )
    conn.commit()
    print("Добавлен студент:", name, email)

def add_new_course(conn: sqlite3.Connection, title: str):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO courses(title) VALUES(?);",
        (title,)
    )
    conn.commit()
    print("Добавлен курс: ", title)

def add_student_to_course(conn: sqlite3.Connection, email: str, course_title: str):
    cur = conn.cursor()
    course = cur.execute("SELECT id FROM courses WHERE title = ?;", (course_title,)).fetchone()
    student = cur.execute("SELECT id FROM students WHERE email =?;", (email,)).fetchone()
    student_name = cur.execute("SELECT name FROM students WHERE email =?;", (email,)).fetchone()[0]
    cur.execute(
        "INSERT INTO enrollments (course_id, student_id) VALUES (?, ?);",
        (course[0], student[0])
    )
    conn.commit()
    print(f"Добавлен студент {student_name} на {course_title} курс")

create_table_students(conn)
create_table_courses(conn)
create_table_enrollments(conn)

add_new_course(conn, "Math")
add_new_course(conn, "Physics")

add_new_student(conn, "Yana", "yana@mail.com")

add_student_to_course(conn, "yana@mail.com", "Math")

conn.commit()
conn.close()