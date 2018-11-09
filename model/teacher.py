class Teacher:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.semesters_courses = []

    def teach(self, semester_course):
        self.semesters_courses.append(semester_course)
        semester_course.add_teacher(self)

    def __str__(self):
        return "\nId: %s, FirstName: %s, LastName:%s" % (
            self.id, self.firstname, self.lastname)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return (self.id) == (other.id)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)
