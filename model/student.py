class Student:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.semesters_courses_quizes = {}

    def enroll(self, semester_course):
        self.semesters_courses_quizes[semester_course] = []
        semester_course.add_student(self)

    def assign_quiz(self, semester_course, quiz):
        self.semesters_courses_quizes[semester_course].append(quiz)

    def print_quiz(self, semester_course, quiz_num):
        print(self.semesters_courses_quizes[semester_course][quiz_num - 1])

    def grade_quiz(self, semester_course, quiz_num):
        return self.semesters_courses_quizes[semester_course][quiz_num -
                                                              1].grade()

    def accumulate_grade(self, semester_course):
        num_quizes = len(self.semesters_courses_quizes[semester_course])
        grade_accumulator = 0
        for quiz in self.semesters_courses_quizes[semester_course]:
            grade_accumulator = grade_accumulator + quiz.grade()
        return grade_accumulator / num_quizes

    def answer_quiz(self, semester_course, quiz_num, question_num, answers):
        self.semesters_courses_quizes[semester_course][quiz_num - 1].answer(
            question_num, answers)

    def __str__(self):
        return "\nid: %s, FirstName: %s, LastName: %s" % (
            self.id, self.firstname, self.lastname)
