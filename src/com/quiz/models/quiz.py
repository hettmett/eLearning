from sqlalchemy import Column, String, Integer, Boolean, String
from models.base import Base, DB


class Questions(Base):
    """Mapping for questions table."""

    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer)  # ForeignKey('lessons.id')
    question = Column(String)

    @staticmethod
    def add(lesson_id, question):
        """Adding record to the table."""
        try:
            question = Questions(lesson_id=lesson_id,
                                 question=question)
            DB.add(question)
            DB.commit()
            return question.id
        except Exception:
            DB.rollback()

    @staticmethod
    def get_by_lessons(lesson_ids: set):
        """Selecting questions by lesson_ids."""
        try:
            return DB.query(Questions).filter(
                Questions.lesson_id.in_(lesson_ids)
            ).all()

        except Exception:
            return 'bad'
            DB.rollback()

    @staticmethod
    def remove(id: int):
        """Removing the record from the table."""
        try:
            DB.remove(Questions.find_by_id(id))
        except Exception:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        """Finding tha record in the table by id."""
        try:
            return DB.query(Questions).filter(Questions.id == id).first()
        except Exception:
            DB.rollback()

    def __repr__(self):
        """Representation of single row."""
        return "lesson_id = {}\n" \
               "question = {}".format(self.lesson_id,
                                      self.question)


class Answers(Base):
    """Mapping for answers table."""

    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer)
    answer = Column(String)
    is_right = Column(Boolean)

    @staticmethod
    def add(question_id, answer, is_right):
        """Adding record to the table."""
        try:
            DB.add(Answers(question_id=question_id,
                           answer=answer,
                           is_right=is_right))
            DB.commit()
        except Exception:
            DB.rollback()

    @staticmethod
    def remove(id: int):
        """Removing the record from the table."""
        try:
            DB.remove(Answers.find_by_id(id))
        except Exception:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        """Finding tha record in the table by id."""
        try:
            return DB.query(Answers).filter(Answers.id == id).first()
        except Exception:
            DB.rollback()

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
    title = Column(String)
    lessons = Column(String)
    start_time = Column(String)
    duration = Column(Integer)
    create_date = Column(String)
    modified_date = Column(String)
    count = Column(Integer)

    @staticmethod
    def add(teacher_id, group_id, title, lessons, start_time,
            duration, create_date, count):
        """Adding record to the table."""
        #try:
        quiz = Quizes(teacher_id=teacher_id,
                         group_id=group_id,
                         title=title,
                         lessons=lessons,
                         start_time=start_time,
                         duration=duration,
                         create_date=create_date,
                         count=count)
        DB.add(quiz)
        DB.commit()
        return quiz.id
        # except Exception:
        #     DB.rollback()



    @staticmethod
    def edit(quiz_id, teacher_id, group_id, title, lessons, start_time,
             duration, modified_date):
        """Adding record to the table."""
        # try:
        DB.query(Quizes).filter(Quizes.id == quiz_id).update(
                                     dict(teacher_id=teacher_id,
                                     group_id=group_id,
                                     title=title,
                                     lessons=lessons,
                                     start_time=start_time,
                                     duration=duration,
                                     modified_date=modified_date)
             )
        DB.commit()
        # except Exception:
        #     DB.rollback()

    @staticmethod
    def remove(id: int):
        """Removing record from the table."""
        try:
            DB.remove(Quizes.find_by_id(id))
        except Exception:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        """Finding record in the table by id."""
        try:
            return DB.query(Quizes).filter(Quizes.id == id).first()
        except Exception:
            DB.rollback()

    @staticmethod
    def all_by_teacher_id(teacher_id: int):
        """Finding record in the table by id."""
        try:
            return DB.query(Quizes).filter(
                Quizes.teacher_id == teacher_id).all()
        except Exception:
            DB.rollback()

    def __repr__(self):
        """Representation of single row."""
        return "teacher_id = {}\n" \
               "group_id = {}\n" \
               "title = {}\n" \
               "lessons = {}\n" \
               "start_time = {}\n" \
               "duration = {}\n" \
               "create_date = {}\n" \
               "modified_date = {}".format(self.teacher_id,
                                           self.group_id,
                                           self.title,
                                           self.lessons,
                                           self.start_time,
                                           self.duration,
                                           self.create_date,
                                           self.modified_date)


class Student_quizes(Base):
    """Mapping for quizes table."""

    __tablename__ = 'student_quizes'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    quiz_id = Column(Integer)
    questions = Column(String)

    @staticmethod
    def add(student_id, quiz_id, questions):
        """Adding record to the table."""
        # try:
        DB.add(Student_quizes(student_id=student_id,
                              quiz_id=quiz_id,
                              questions=questions))
        DB.commit()
        # except Exception:
        #     DB.rollback()

    @staticmethod
    def remove_all_by_quiz_id(quiz_id: int):
        """Removing record from the table."""
        try:
            DB.remove(Student_quizes.all_by_quiz_id(quiz_id))
        except Exception:
            DB.rollback()

    @staticmethod
    def all_by_quiz_id(quiz_id: int):
        """Finding record in the table by id."""
        try:
            return DB.query(Student_quizes).\
                filter(Student_quizes.quiz_id == quiz_id).all()
        except Exception:
            DB.rollback()

    def __repr__(self):
        """Representation of single row."""
        return "student_id = {}\n" \
               "questions = {}".format(self.teacher_id,
                                       self.quiz_id,
                                       self.questions)


class Quiz_submission(Base):
    """Mapping for quiz_submission table."""

    __tablename__ = 'quiz_submission'

    id = Column(Integer, primary_key=True)
    student_quiz_id = Column(Integer)
    start_date = Column(String)
    submission_date = Column(String)
    rate = Column(Integer)

    @staticmethod
    def add(student_quiz_id, start_date, submission_date):
        """Adding record to the table."""
        try:
            DB.add(Quiz_submission(student_quiz_id=student_quiz_id,
                                   start_date=start_date,
                                   submission_date=submission_date))
            DB.commit()
        except Exception:
            DB.rollback()

    def __repr__(self):
        """Representation of single row."""
        return "student_quiz_id = {}\n" \
               "start_date = {}\n" \
               "submission_date = {}".format(self.student_quiz_id,
                                             self.start_date,
                                             self.submission_date)


class Submitted_answers(Base):
    """Mapping for submitted_answers table."""

    __tablename__ = 'submitted_answers'

    id = Column(Integer, primary_key=True)
    submission_id = Column(Integer)
    answer_id = Column(Integer)

    @staticmethod
    def add(submission_id, answer_id):
        """Adding record to the table."""
        try:
            DB.add(Submitted_answers(submission_id=submission_id,
                                     answer_id=answer_id))
            DB.commit()
        except Exception:
            DB.rollback()

    def __repr__(self):
        """Representation of single row."""
        return "submission_id = {}\n" \
               "answer_id = {}".format(self.submission_id,
                                       self.answer_id)


if __name__ == "__main__":
    question = Questions(question='What is the capital of Austria?')
    print(question.question)
    DB.add(question)
    answer = Answers(question_id=1, answer='Vienna', is_right=1)
    print(answer.answer, answer.is_right)
    DB.add(answer)
    quiz = Quizes(start_time=String.now())
    print(quiz.start_time)
    DB.add(quiz)
    DB.commit()
    print(answer.id)
