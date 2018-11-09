Feature: Student Enrolloment, Quiz Taking And Grading

  Scenario: Grade Students Enrolled In Classes
     Given we have the following students
     |student_id| firstname  | lastname|
     |1         | Joe        | Bar     |
     |2         | Mark       | Jack    |

     Given we have the following teachers
     |teacher_id| firstname  | lastname |
     |1         | Sam        | Mark     |
     |2         | John       | Doe      |

     Given we have the following courses
     |course_name| credit  |
     | CRS-1     | 4       |
     | CRS-2     | 4       |
     
     Given the following teachers teach classes in the given semesters
     |class_id |course_name| teacher_id  | session   | year |
     |1        | CRS-1     | 1           | SPRING    | 2003 |
     |2        | CRS-2     | 2           | SPRING    | 2003 |

     Given the following students are enrolled in the following classes
     |class_id |student_id| 
     |1        | 1        |
     |1        | 2        |
     |2        | 1        |

    Given we have the following question sets
     |question_set_id  | question               | options                      | expected_answers |
     |1                | what is the dog's name | {'A': 'Jack', 'B': 'Jango'}  | ['A']            |
     |1                | what is the cat's name | {'A': 'Jack', 'B': 'Jango'}  | ['B']            |
     |2                | what is the car's color| {'A': 'Blue', 'B': 'Black'}  | ['A']            |
     |2                | what is the house color| {'A': 'White', 'B': 'Brown'} | ['B']            |
     |3                | what is the bird's name| {'A': 'coocoo', 'B': 'Kate'} | ['B']            |

    Given that students in classes are assigned the given question sets
    |class_id |question_set_id| 
    |1        | 1             |
    |1        | 2             |
    |2        | 3             |
    
    When the students answers the following assigned quiz questions
    |class_id |quiz_assingment_num  | student_id  | question_num| selected_answer |
    |1        | 1                   | 1           | 1           | ['A']           |
    |1        | 1                   | 1           | 2           | ['B']           |
    |1        | 2                   | 1           | 1           | ['A']           |
    |1        | 2                   | 1           | 2           | ['B']           |
    |1        | 1                   | 2           | 1           | ['A']           |
    |1        | 1                   | 2           | 2           | ['A']           |
    |1        | 2                   | 2           | 1           | ['A']           |
    |1        | 2                   | 2           | 2           | ['B']           |
    |2        | 1                   | 1           | 1           | ['B']           |

    Then the following students grade report should show
    |class_id |student_id| quiz_assingment_num | grade |
    |1        | 1        | 1                   | 100.0 |
    |1        | 1        | 2                   | 100.0 |
    |1        | 2        | 1                   | 50.0  |
    |1        | 2        | 2                   | 100.0 |
    |2        | 1        | 1                   | 100.0 |

    Then the following students accumulated grade report should show
    |class_id |student_id| accumulated_grade |
    |1        | 1        | 100.0             |
    |1        | 2        | 75.0              |
    |2        | 1        | 100.0             |
