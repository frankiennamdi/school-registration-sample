from model.course import Course
from model.teacher import Teacher
from model.student import Student
from model.question import Question
import pytest


@pytest.fixture
def quiz1():
    return [
        Question("what is the dog's name", {
            'A': 'Jack',
            'B': 'Jango'
        }, ['A']),
        Question("what is the cat's name", {
            'A': 'Jack',
            'B': 'Jango'
        }, ['B'])
    ]


@pytest.fixture
def quiz2():
    return [
        Question("what is the car's color", {
            'A': 'Blue',
            'B': 'Black'
        }, ['A']),
        Question("what is the house's color", {
            'A': 'White',
            'B': 'Brown'
        }, ['B'])
    ]

def test_student_enrollment_quiz_taking_and_grading(quiz1, quiz2):
    teacher_sam = Teacher(1, "Sam", "Doe")
    student1 = Student(1, "Joe", "Bar")
    course = Course("MATH_101", 4)
    spring_2003_math_101 = course.add_class("SPRING", 2003, teacher_sam)
    student1.enroll(spring_2003_math_101)

    spring_2003_math_101.assign_quiz(quiz1)
    spring_2003_math_101.assign_quiz(quiz2)
    
    student1.answer_quiz(spring_2003_math_101, 1, 1, ['A'])
    student1.answer_quiz(spring_2003_math_101, 1, 2, ['B'])
    student1.answer_quiz(spring_2003_math_101, 2, 1, ['A'])
    student1.answer_quiz(spring_2003_math_101, 2, 2, ['A'])
    
    student1.grade_quiz(spring_2003_math_101, 1) == 100.0
    student1.grade_quiz(spring_2003_math_101, 2) == 50.0

    assert student1.accumulate_grade(spring_2003_math_101) == 75.0
