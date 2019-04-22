class StudentCourseError(Exception):
    pass


class Student:
    def __init__(self, full_name, course_name=None):
        self.full_name = full_name
        self.course_name = course_name
        self.course_num = 1
    
    def next_course(self):
        if self.course_name is None:
            raise StudentCourseError('Not have course') 
        elif self.course_num >= 3:
            raise StudentCourseError('Student have degree') 
        else:
            self.course_num += 1
    

    def change_course(self, course_name):
        self.course_name = course_name
        self.course_num = 1

    
    def get_diploma(self):
        if self.course_num < 3:
            raise StudentCourseError('Student not have degree')
        else:
            return '{},{}'.format(self.full_name, self.course_name)
