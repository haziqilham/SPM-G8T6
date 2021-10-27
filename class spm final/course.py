class Course():
    __course_id = 0
    __course_name = None
    __archive_date = None

    def __init__(self, id, name, date):
        self.__course_id = id
        self.__course_name = name
        self.__archive_date = date

    #Getter Methods
    def getId(self):
        return self.__course_id
    def getCourseName(self):
        return self.__course_name
    def getArchiveDate(self):
        return self.__archive_date

    #Setter Methods
    def setCourseName(self, name):
        self.__course_name = name
        return self.__course_name
    def setArchiveDate(self, date):
        self.__archive_date = date
        return self.__archive_date

    def createCourse(self, id, name, date):
        course = self.__init__(id, name, date)
        return course.getId()