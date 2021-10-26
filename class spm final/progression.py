class Progression():
    __cc_id = 0
    __status = None
    __completion_date = None
    __score = None

    def __init__(self, id, status, date, score):
        self.__cc_id = id
        self.__status = status
        self.__completion_date = date
        self.__score = score

    #Getter Methods
    def getId(self):
        return self.__course_id
    def getStatus(self):
        return self.__status
    def getCompletionDate(self):
        return self.__completion_date
    def getScore(self):
        return self.__score

    #Setter Methods
    def setStatus(self, status):
        self.__status = status
        return self.__status
    def setCompletionDate(self, date):
        self.__completion_date = date
        return self.__completion_date
    def setScore(self, score):
        self.__score = score
        return self.__score