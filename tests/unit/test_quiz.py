from model.question import Question
from model.quiz import Quiz
import pytest


@pytest.fixture
def question1():
    return Question("what is the dog's name", {'A': 'Jack', 'B': 'Jango'}, ['A'])

@pytest.fixture
def question2():
    return Question("what is the cat's name", {'A': 'Jack', 'B': 'Jango'}, ['B'])

@pytest.fixture
def question3():
    return Question("what is the bird's name", {'A': 'Jack', 'B': 'Mark'}, ['B'])


def test_quiz_with_valid_answer(question1, question2):
    questions = [question1, question2]
    quiz = Quiz(questions)
    quiz.answer(1, ['A'])
    quiz.answer(2, ['B'])
    print(quiz)
    grade = quiz.grade()
    print("Grade: {}".format(grade))
    assert grade == 100.0

def test_quiz_with_one_invalid_answer(question1, question2, question3):
    questions = [question1, question2, question3]
    quiz = Quiz(questions)
    quiz.answer(1, ['A'])
    quiz.answer(2, ['B'])
    quiz.answer(3, ['A'])
    print(quiz)
    grade = quiz.grade()
    print("Grade: {}".format(grade))
    assert grade == 66.67
    
def test_that_question_with_wrong_expected_answers_list_raises_exception():
    with pytest.raises(Exception):
        Question("what is the cat name", {'A': 'Jack', 'B': 'Jango'}, ['D'])

def test_that_question_with_no_selected_answers_returns_none(question1):
    print(question1)
    assert question1.is_answer_correct() == None

def test_question_with_valid_selected_answers(question1, question2):

    question1.answer(['A'])
    question2.answer(['B'])
    print(question1)
    print(question2)
    assert question1.is_answer_correct() == True
    assert question2.is_answer_correct() == True

def test_question_with_invalid_selected_answers(question1, question2):

    question1.answer(['B'])
    question2.answer(['A'])
    print(question1)
    print(question2)
    assert question1.is_answer_correct() == False
    assert question2.is_answer_correct() == False
