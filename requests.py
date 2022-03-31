from model import Group, Grade, Student, session
from sqlalchemy.sql import func


def task_1():
    print('5 студентов с наибольшим средним баллом по всем предметам.')
    qs = session.query(Grade.student_first_name, func.avg(Grade.grad))\
        .group_by(Grade.student_first_name).order_by(func.avg(Grade.grad).desc()).limit(5)
    for i in qs:
        print(i)
    print('-' * 100)


def task_2():
    print('1 студент с наивысшим средним баллом по одному предмету.')
    qs = session.query(Grade.subject_name, Grade.student_first_name, func.avg(Grade.grad)).group_by(Grade.student_first_name)\
        .group_by(Grade.subject_name).order_by(func.avg(Grade.grad).desc()).limit(1)
    for i in qs:
        print(i)
    print('-' * 100)


def task_3():
    print('средний балл в группе по одному предмету.')
    qs = session.query(Student.group_name, Grade.subject_name, func.avg(Grade.grad)).join(Student).join(Group)\
        .filter(Grade.subject_name == 'subject2').filter(Group.name == 'group1').group_by(Grade.subject_name).group_by(Group.name).order_by(Group.name)
    for i in qs:
        print(i)
    print('-' * 100)


def task_4():
    print('Средний балл в потоке.')
    qs = session.query(func.avg(Grade.grad))
    for i in qs:
        print(i)
    print('-' * 100)


def task_5():
    print('Какие курсы читает преподаватель.')
    qs = session.query(Grade.teacher_first_name, Grade.subject_name).filter(Grade.teacher_first_name == 'Bill')\
        .distinct().order_by(Grade.teacher_first_name)
    for i in qs:
        print(i)
    print('-' * 100)


def task_6():
    print('Список студентов в группе.')
    qs = session.query(Student.group_name, Student.first_name).filter(Student.group_name == 'group3')\
        .order_by(Student.group_name.desc())
    for i in qs:
        print(i)
    print('-' * 100)


def task_7():
    print('Оценки студентов в группе по предмету.')
    qs = session.query(Student.group_name, Grade.subject_name, Grade.student_first_name, Grade.grad).join(Student)\
        .filter(Student.group_name == 'group1').filter(Grade.subject_name == 'subject2')
    for i in qs:
        print(i)
    print('-' * 100)


def task_8():
    print('Оценки студентов в группе по предмету на последнем занятии.')
    qs = session.query(Student.group_name, Grade.subject_name, Grade.student_first_name, Grade.grad, Grade.create_time).join(Student)\
        .filter(Student.group_name == 'group1').filter(Grade.subject_name == 'subject2').order_by(Grade.create_time.desc())\
        .limit(5)
    for i in qs:
        print(i)
    print('-' * 100)


def task_9():
    print('Средний балл, который преподаватель ставит студенту.')
    qs = session.query(Grade.student_first_name, Grade.teacher_first_name, func.avg(Grade.grad))\
        .filter(Grade.student_first_name == 'Student10').filter(Grade.teacher_first_name == 'Bill').distinct()
    for i in qs:
        print(i)
    print('-' * 100)


def task_10():
    print('Средний балл, который ставит преподаватель.')
    qs = session.query(Grade.teacher_first_name, func.avg(Grade.grad))\
        .filter(Grade.teacher_first_name == 'Bill').distinct()
    for i in qs:
        print(i)
    print('-' * 100)


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()