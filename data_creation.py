from model import Group, Grade, Student, Teacher, Subject, session
from datetime import timedelta
import random
import datetime

Now = datetime.datetime.now()

teacher_rows = [Teacher(first_name='Ted'), Teacher(first_name='Bill'), Teacher(first_name='Bob')]
subject_rows = [Subject(name='subject1'), Subject(name='subject2'), Subject(name='subject3'), Subject(name='subject4'),
                Subject(name='subject5')]
group_rows = [Group(name='group1'), Group(name='group2'), Group(name='group3')]


def create_students():
    students = []
    student = 0
    while student < 30:
        student = student + 1
        first_name = f'Student{student}'
        group_id = random.randint(1, 3)
        group = session.query(Group).get(group_id)
        students.append(Student(first_name=first_name, group=group))
    return students


def create_grades():
    grades = []
    id = 0
    st = 0
    while st < 30:
        st = st + 1
        gr = 0
        while gr < 20:
            gr = gr + 1
            id = id + 1
            grad = random.randint(1, 5)
            create_time = Now + timedelta(days=grad)
            subject_id = random.randint(1, 5)
            student_id = st
            teacher_id = random.randint(1, 3)
            student = session.query(Student).get(student_id)
            teacher = session.query(Teacher).get(teacher_id)
            subject = session.query(Subject).get(subject_id)
            grades.append(Grade(grad=grad, create_time=create_time, subject=subject, student=student,
                           teacher=teacher))
    return grades


if __name__ == '__main__':
    session.add_all(teacher_rows)
    session.add_all(subject_rows)
    session.add_all(group_rows)
    session.add_all(create_students())
    session.add_all(create_grades())
    session.commit()