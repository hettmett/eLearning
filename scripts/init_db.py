import sqlite3
from datetime import datetime


print('Creating Database schema at: {}'.format(datetime.now()))
con = sqlite3.connect("app.db")
cur = con.cursor()

try:
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS users(
            id integer PRIMARY KEY,
            email text,
            pwd text,
            f_name text,
            l_name text,
            m_name text,
            birth_date text,
            role text,
            create_date text DEFAULT (datetime('now','localtime')),
            token text
        );

        CREATE TABLE IF NOT EXISTS courses(
            id integer PRIMARY KEY,
            course_name text,
            description text,
            create_date text DEFAULT (datetime('now','localtime'))
        );

        CREATE TABLE IF NOT EXISTS groups(
            id integer PRIMARY KEY,
            group_name text,
            course_id integer,
            start_date text,
            end_date text,
            create_date text DEFAULT (datetime('now','localtime')),
            modified text,
            teacher_id integer,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        );

        CREATE TABLE IF NOT EXISTS group_students(
            id integer PRIMARY KEY,
            group_id integer,
            user_id integer,
            active integer,
            create_date text DEFAULT (datetime('now','localtime')),
            FOREIGN KEY (group_id) REFERENCES groups(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS lessons(
            id integer PRIMARY KEY,
            group_id integer,
            title text,
            description text,
            file_path text,
            lesson_date text,
            FOREIGN KEY (group_id) REFERENCES groups(id)
        );

        CREATE TABLE IF NOT EXISTS homeworks(
            id integer PRIMARY KEY,
            lesson_id integer,
            title text,
            description text,
            file_path text,
            deadline text,
            FOREIGN KEY (lesson_id) REFERENCES lessons(id)
        );

        CREATE TABLE IF NOT EXISTS completed_homeworks(
            id integer PRIMARY KEY,
            homework_id integer,
            user_id integer,
            file_path text,
            description text,
            submission_date text DEFAULT (datetime('now','localtime')),
            checked integer,
            rate integer,
            FOREIGN KEY (homework_id) REFERENCES homeworks(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS questions(
            id integer PRIMARY KEY,
            lesson_id integer,
            question text NOT NULL,
            FOREIGN KEY (lesson_id) REFERENCES lessons(id)
        );

        CREATE TABLE IF NOT EXISTS answers(
            id integer PRIMARY KEY,
            question_id integer,
            answer text NOT NULL,
            is_right integer,
            FOREIGN KEY (question_id) REFERENCES questions(id)
        );

        CREATE TABLE IF NOT EXISTS quizes(
            id integer PRIMARY KEY,
            teacher_id integer,
            group_id integer,
            student_id integer,
            start_time text,
            duration text,
            questions text,
            FOREIGN KEY (teacher_id) REFERENCES users(id),
            FOREIGN KEY (student_id) REFERENCES users(id),
            FOREIGN KEY (group_id) REFERENCES groups(id)
        );

        CREATE TABLE IF NOT EXISTS quiz_submission(
            id integer PRIMARY KEY,
            student_id integer,
            quiz_id integer,
            start_date text,
            submission_date text DEFAULT (datetime('now','localtime')),
            FOREIGN KEY (student_id) REFERENCES users(id),
            FOREIGN KEY (quiz_id) REFERENCES quizes(id)
        );

        CREATE TABLE IF NOT EXISTS submitted_answers(
            id integer PRIMARY KEY,
            submission_id integer,
            answer_id integer,
            FOREIGN KEY (submission_id) REFERENCES quiz_submission(id),
            FOREIGN KEY (answer_id) REFERENCES answers(id)
        )
        """)
    con.commit()
    print('Database schema created at: {}'.format(datetime.now()))
except Exception as err:
    print("ERROR: {}".format(str(err)))
    con.rollback()
finally:
    con.close()
