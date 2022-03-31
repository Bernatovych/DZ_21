from sqlalchemy import DateTime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    group_name = Column(Integer, ForeignKey('groups.name'))
    group = relation(Group, backref='groups')


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grad = Column(Integer)
    create_time = Column(DateTime)
    subject_name = Column(Integer, ForeignKey('subjects.name'))
    teacher_first_name = Column(Integer, ForeignKey('teachers.first_name'))
    student_first_name = Column(Integer, ForeignKey("students.first_name"))
    subject = relation(Subject, backref='subjects')
    teacher = relation(Teacher, backref='teachers')
    student = relation(Student, backref='students')


engine = create_engine("sqlite:///test.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

