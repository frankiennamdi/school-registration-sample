class Question:
    def __init__(self, text, choices, expected_answers):
        self.text = text
        self.selected_answers = []
        if set(expected_answers).issubset(set(choices.keys())):
            self.choices = choices
            self.expected_answers = expected_answers
        else:
            raise Exception(
                "expected_answers {} contains selections not in choices keys {}"
                .format(expected_answers, choices.keys()))
        self.selections = []

    def answer(self, selected_answers):
        self.selected_answers = selected_answers

    def is_answer_correct(self):
        if not self.selected_answers:
            return None
        else:
            return self.expected_answers == self.selected_answers

    def __str__(self):
        options = []
        for key, value in self.choices.items():
            options.append("{}. {}".format(key, value))
        return "\nQuestion: %s\nOptions: \n%s\nExpected Answers: \n%s\nSelected Answers: \n%s" % (
            self.text, "\n".join(options), ",".join(
                self.expected_answers), ",".join(self.selected_answers))
