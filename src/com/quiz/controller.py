import json
import random
from com.groups.models.group_student import Group_student
from com.quiz.models.quiz import Questions, Quizes, Student_quizes, Answers
from flask import flash


class QuizController(object):
    def __init__(self):
        super().__init__()

    def add_question(self, id, question, answers, right_ans):
        question_id = Questions.add(id, question)
        for num, ans in enumerate(answers, 1):
            if int(right_ans) == num:
                Answers().add(question_id, ans, 1)
            else:
                Answers().add(question_id, ans, 0)

    def questions_sampling(self, lessons: list, count: int) -> list:
        # Selecting questions by lessons and sampling to requied amount
        questions = Questions.get_by_lessons(lessons)
        questions = list(questions)
        selected_questions = random.sample(questions, count)
        quiz = []
        for i in range(count):
            quiz.append(selected_questions[i].id)
        return quiz

    def generate_quiz(self, teacher_id: int, group_id: int, title: str,
                      lessons: list, start_time: str, create_date: str,
                      duration: str, count: str):
        # adding metadata to Quiz table
        lessons = json.dumps(lessons)
        quiz_id = Quizes.add(teacher_id, group_id, title, lessons,
                             start_time, duration, create_date, count)

        # Selecting questions and writing quizes to Student_quizes table
        group_students = Group_student().get_student(group_id)
        for student in group_students:
            questions = json.dumps(self.questions_sampling(lessons, count))
            Student_quizes.add(int(student.id), quiz_id, questions)


    def get_all(self, teacher_id):
        return Quizes().all_by_teacher_id(teacher_id)

    def find_by_id(self, id):
        return Quizes.find_by_id(id)

    def edit(self, quiz_id, teacher_id, group_id, title, lessons,
             start_time, modified_date, duration):
        # editing data in Quiz table
        Quizes().edit(quiz_id, teacher_id, group_id, title,
                      lessons, start_time, duration, modified_date)
        # Student_quizes().remove(quiz_id)
