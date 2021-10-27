import datetime as dt

class Chapter():
    __class_id = 0
    __class_name = None
    __capacity = 0
    __trainer = 0
    __start_date = dt.date(0,0,0)
    __end_date = dt.date(0,0,0)
    __start_time = dt.time(0,0)
    __end_time = dt.time(0,0)
    __start_enrollment = dt.date(0,0,0)
    __end_enrollment = dt.date(0,0,0)

    def __init__(self, id, name, capacity, trainer, startdate, enddate, starttime, endtime, startenroll, endenroll):
        self.__class_id = id
        self.__class_name = name
        self.__capacity = capacity
        self.__trainer = trainer
        self.__start_date = startdate
        self.__end_date = enddate
        self.__start_time = starttime
        self.__end_time = endtime
        self.__start_enrollment = startenroll
        self.__end_enrollment = endenroll

    #getter methods
    def getClassId(self):
        return self.__class_id
    def getClassName(self):
        return self.__class_name
    def getCapacity(self):
        return self.__capacity
    def getTrainer(self):
        return self.__trainer
    def getStartdate(self):
        return self.__start_date
    def getEnddate(self):
        return self.__end_date
    def getStarttime(self):
        return self.__start_time
    def getEndtime(self):
        return self.__end_time
    def getStartEnroll(self):
        return self.__start_enrollment
    def getEndenroll(self):
        return self.__end_enrollment

    #setter methods
    def setClassName(self, name):
        self.__class_name = name
        return self.__class_name
    def setCapacity(self, capacity):
        self.__capacity = capacity
        return self.__capacity
    def setTrainer(self, trainer):
        self.__trainer = trainer
        return self.__trainer
    def setStartdate(self, date):
        self.__start_date = date
        return self.__start_date
    def setEnddate(self, date):
        self.__end_date = date
        return self.__end_date
    def setStarttime(self, time):
        self.__start_time = time
        return self.__start_time
    def setEndtime(self, time):
        self.__end_time = time
        return self.__end_time
    def setStartEnroll(self, date):
        self.__start_enrollment = date
        return self.__start_enrollment
    def setEndenroll(self, date):
        self.__end_enrollment = date
        return self.__end_enrollment

    