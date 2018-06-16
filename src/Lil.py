from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime import datetime
from random import randint, sample
import json

Base = declarative_base()
engine = create_engine("sqlite:///app.db")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Questions(Base):
    """Mapping for questions table."""

    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer)  # ForeignKey('lessons.id')
    question = Column(String)

    def __repr__(self):
        """Representation of single row."""
        return "lesson_id = {}\n" \
               "question = {}".format(self.lesson_id,
                                      self.question)


class Answers(Base):
    """Mapping for answers table."""

    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer = Column(String)
    is_right = Column(Boolean)

    def __repr__(self):
        """Representation of single row."""
        return "question_id = {}\n" \
               "answer = {}\n" \
               "is_right = {}".format(self.question_id,
                                      self.answer,
                                      self.is_right)


class Quizes(Base):
    """Mapping for quizes table."""

    __tablename__ = 'quizes'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer)
    group_id = Column(Integer)
    student_id = Column(Integer)
    start_time = Column(DateTime)
    duration = Column(Integer)
    questions = Column(String)

    def __repr__(self):
        """Representation of single row."""
        return "teacher_id = {}\n" \
               "group_id = {}\n" \
               "student_id = {}\n" \
               "start_time = {}\n" \
               "duration = {}\n" \
               "question = {}".format(self.teacher_id,
                                      self.group_id,
                                      self.student_id,
                                      self.start_time,
                                      self.duration,
                                      self.question)


class Quiz_submission(Base):
    """Mapping for quiz_submission table."""

    __tablename__ = 'quiz_submission'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    quiz_id = Column(Integer)
    start_date = Column(DateTime)
    submission_date = Column(DateTime)

    def __repr__(self):
        """Representation of single row."""
        return "student_id = {}\n" \
               "quiz_id = {}\n" \
               "start_date = {}\n" \
               "submission_date = {}".format(self.student_id,
                                             self.quiz_date,
                                             self.start_date,
                                             self.submission_date)


class Submitted_answers(Base):
    """Mapping for submitted_answers table."""

    __tablename__ = 'submitted_answers'

    id = Column(Integer, primary_key=True)
    submission_id = Column(Integer)
    answer_id = Column(Integer)

    def __repr__(self):
        """Representation of single row."""
        return "submission_id = {}\n" \
               "answer_id = {}".format(self.submission_id,
                                       self.answer_id)


with open('data.json') as js:
    data = js.read()
    decoded = json.loads(data)

for key, value in decoded.items():
    question = Questions(question='What is the capital of {}?'.format(key),
                         lesson_id=randint(1, 4))
    print(question.question)
    session.add(question)
    session.commit()
    answer = Answers(answer=value, is_right=True, question_id=question.id)
    session.add(answer)
    session.commit()
    print(answer.id)
    while True:
        wrong_answers = sample(list(decoded.values()), 3)
        if value not in wrong_answers:
            break
    for wrong_answer in wrong_answers:
        answer = Answers(answer=wrong_answer,
                         is_right=False,
                         question_id=question.id)
        session.add(answer)
        session.commit()