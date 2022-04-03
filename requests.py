from model import Group, Grade, Student, session
from sqlalchemy.sql import func


def five_students_with_a_high_average_score_in_all_subjects():
    print('five_students_with_a_high_average_score_in_all_subjects.')
    qs = session.query(Grade.student_first_name, func.avg(Grade.grad))\
        .group_by(Grade.student_first_name).order_by(func.avg(Grade.grad).desc()).limit(5)
    for i in qs:
        print(i)
    print('-' * 100)


def one_student_with_the_highest_average_score_in_one_subject():
    print('one_student_with_the_highest_average_score_in_one_subject.')
    qs = session.query(Grade.subject_name, Grade.student_first_name, func.avg(Grade.grad)).group_by(Grade.student_first_name)\
        .group_by(Grade.subject_name).order_by(func.avg(Grade.grad).desc()).limit(1)
    for i in qs:
        print(i)
    print('-' * 100)


def average_score_in_the_group_in_one_subject():
    print('average_score_in_the_group_in_one_subject.')
    qs = session.query(Student.group_name, Grade.subject_name, func.avg(Grade.grad)).join(Student).join(Group)\
        .filter(Grade.subject_name == 'subject2').filter(Group.name == 'group1').group_by(Grade.subject_name).group_by(Group.name).order_by(Group.name)
    for i in qs:
        print(i)
    print('-' * 100)


def average_score_in_the_stream():
    print('average_score_in_the_stream.')
    qs = session.query(func.avg(Grade.grad))
    for i in qs:
        print(i)
    print('-' * 100)


def what_courses_does_the_teacher_teach():
    print('what_courses_does_the_teacher_teach.')
    qs = session.query(Grade.teacher_first_name, Grade.subject_name).filter(Grade.teacher_first_name == 'Bill')\
        .distinct().order_by(Grade.teacher_first_name)
    for i in qs:
        print(i)
    print('-' * 100)


def list_of_students_in_the_group():
    print('list_of_students_in_the_group.')
    qs = session.query(Student.group_name, Student.first_name).filter(Student.group_name == 'group3')\
        .order_by(Student.group_name.desc())
    for i in qs:
        print(i)
    print('-' * 100)


def grades_of_students_in_the_group_in_the_subject():
    print('grades_of_students_in_the_group_in_the_subject.')
    qs = session.query(Student.group_name, Grade.subject_name, Grade.student_first_name, Grade.grad).join(Student)\
        .filter(Student.group_name == 'group1').filter(Grade.subject_name == 'subject2')
    for i in qs:
        print(i)
    print('-' * 100)


def grades_of_students_in_group_on_subject_at_last_lesson():
    print('grades_of_students_in_group_on_subject_at_last_lesson.')
    qs = session.query(Student.group_name, Grade.subject_name, Grade.student_first_name, Grade.grad, Grade.create_time).join(Student)\
        .filter(Student.group_name == 'group1').filter(Grade.subject_name == 'subject2').order_by(Grade.create_time.desc())\
        .limit(5)
    for i in qs:
        print(i)
    print('-' * 100)


def the_average_score_that_the_teacher_gives_to_the_student():
    print('the_average_score_that_the_teacher_gives_to_the_student.')
    qs = session.query(Grade.student_first_name, Grade.teacher_first_name, func.avg(Grade.grad))\
        .filter(Grade.student_first_name == 'Student10').filter(Grade.teacher_first_name == 'Bill').distinct()
    for i in qs:
        print(i)
    print('-' * 100)


def the_average_score_given_by_the_teacher():
    print('the_average_score_given_by_the_teacher')
    qs = session.query(Grade.teacher_first_name, func.avg(Grade.grad))\
        .filter(Grade.teacher_first_name == 'Bill').distinct()
    for i in qs:
        print(i)
    print('-' * 100)


if __name__ == '__main__':
    five_students_with_a_high_average_score_in_all_subjects()
    one_student_with_the_highest_average_score_in_one_subject()
    average_score_in_the_group_in_one_subject()
    average_score_in_the_stream()
    what_courses_does_the_teacher_teach()
    list_of_students_in_the_group()
    grades_of_students_in_the_group_in_the_subject()
    grades_of_students_in_group_on_subject_at_last_lesson()
    the_average_score_that_the_teacher_gives_to_the_student()
    the_average_score_given_by_the_teacher()