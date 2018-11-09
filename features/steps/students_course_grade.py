# pylint: disable=undefined-variable
import behave
from model.question import Question
from model.student import Student
from model.teacher import Teacher
from model.course import Course
import ast
from itertools import chain


@given('we have the following students')
def we_have_the_following_students(context):
    students = {}
    for row in context.table:
        student_id = row['student_id']
        firstname = row['firstname']
        lastname = row['lastname']
        students[student_id] = Student(student_id, firstname, lastname)
    context.students = students
    for value in students.values():
        print(str(value))
    pass


@given('we have the following teachers')
def we_have_the_following_teachers(context):
    teachers = {}
    for row in context.table:
        teacher_id = row['teacher_id']
        firstname = row['firstname']
        lastname = row['lastname']
        teachers[teacher_id] = Teacher(teacher_id, firstname, lastname)
    context.teachers = teachers
    for value in teachers.values():
        print(str(value))
    pass


@given('we have the following courses')
def we_have_the_following_courses(context):
    courses = {}
    for row in context.table:
        course_name = row['course_name']
        credit = row['credit']
        courses[course_name] = Course(course_name, credit)
    context.courses = courses
    for value in courses.values():
        print(str(value))
    pass


@given('the following teachers teach classes in the given semesters')
def teacher_teaches_courses_in_semester(context):
    course_classes = {}
    for row in context.table:
        class_id = row['class_id']
        course_name = row['course_name']
        teacher_id = row['teacher_id']
        session = row['session']
        year = row['year']
        course = context.courses[course_name]
        teacher = context.teachers[teacher_id]
        course_classes[class_id] = getattr(course, "add_class")(session, year,
                                                                teacher)
    context.course_classes = course_classes

    for value in course_classes.values():
        print(str(value))


@given('the following students are enrolled in the following classes')
def students_enrolled_in_classes(context):

    for row in context.table:
        class_id = row['class_id']
        student_id = row['student_id']
        student = context.students[student_id]
        student.enroll(context.course_classes[class_id])
    for value in context.course_classes.values():
        print(str(value))


@given('we have the following question sets')
def we_have_the_following_quizes(context):
    questions = {}
    for row in context.table:
        question_set_id = row['question_set_id']
        question = row['question']
        options = ast.literal_eval(row['options'])
        expected_answers = ast.literal_eval(row['expected_answers'])
        if question_set_id in questions:
            questions[question_set_id].append(
                Question(question, options, expected_answers))
        else:
            questions[question_set_id] = [
                Question(question, options, expected_answers)
            ]

    for key, value in questions.items():
        print("Quiz {}".format(key))
        print("\nQuestions:\n%s" % ('\n'.join(
            str(question) for question in value)))
    context.questions = questions
    pass


@given('that students in classes are assigned the given question sets')
def assign_question_set_to_students_in_classes(context):
    for row in context.table:
        question_set_id = row['question_set_id']
        class_id = row['class_id']
        course_class = context.course_classes[class_id]
        course_class.assign_quiz(context.questions[question_set_id])


@when('the students answers the following assigned quiz questions')
def the_student_answers_the_quizes(context):
    for row in context.table:
        quiz_assingment_num = row['quiz_assingment_num']
        class_id = row['class_id']
        student_id = row['student_id']
        question_num = row['question_num']
        selected_answer = ast.literal_eval(row['selected_answer'])
        course_class = context.course_classes[class_id]
        context.students[student_id].answer_quiz(course_class, int(quiz_assingment_num),
                                                 int(question_num),
                                                 selected_answer)

@Then('the following students grade report should show')
def the_students_grade_report_should_show(context):
    for row in context.table:
        quiz_assingment_num = row['quiz_assingment_num']
        class_id = row['class_id']
        student_id = row['student_id']
        grade = row['grade']
        student = context.students[student_id]
        assert (student.grade_quiz(context.course_classes[class_id],
                                   int(quiz_assingment_num)) == float(grade))


@Then('the following students accumulated grade report should show')
def the_students_accumulated_grade_report_should_show(context):
    for row in context.table:
        class_id = row['class_id']
        student_id = row['student_id']
        accumulated_grade = row['accumulated_grade']
        student = context.students[student_id]
        assert (student.accumulate_grade(
            context.course_classes[class_id]) == float(accumulated_grade))
