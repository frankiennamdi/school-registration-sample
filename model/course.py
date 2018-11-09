from model.course_class import CourseClass


class Course:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits
        self.semesters = []

    def add_class(self, session, year, teacher):
        semester = CourseClass(self, session, year, teacher)
        self.semesters.append(semester)
        return self.semesters[-1]

    def __str__(self):
        return "\nCourse Name: %s\nCredits: %s" % (self.course_name,
                                                   self.credits)

    def __hash__(self):
        return hash(self.course_name)

    def __eq__(self, other):
        return (self.course_name) == (other.course_name)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)
