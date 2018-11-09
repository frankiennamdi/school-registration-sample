class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def answer(self, question_num, answer_selections):
        self.questions[question_num - 1].answer(answer_selections)

    def grade(self):
        num_correct = 0
        for question in self.questions:
            if (question.is_answer_correct()):
                num_correct = num_correct + 1
        return round((num_correct / len(self.questions)) * 100, 2)

    def __str__(self):
        return "\nQuestions: %s\nGrade: %s" % ('\n'.join(
            str(question) for question in self.questions), self.grade())
