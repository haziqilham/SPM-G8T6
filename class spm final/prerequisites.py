class Prerequisites():
    __prereq_id = 0
    __prereq_course_id = 0

    def __init__(self, id, cid):
        self.__prereq_id = id
        self.__prereq_course_id = cid

    #Getter Methods
    def getId(self):
        return self.__prereq_id
    def getPrereqCourse(self):
        return self.__prereq_course_id