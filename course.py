class Course:
    __courseId=0
    __courseName=None
    __sections=None
    __startDate=None
    __endDate=None
    __prerequisite=None
    __trainer=None
    __learners=None


    def __init__(self, id, name, section, startDate, endDate, prerequisite, trainer, learners):
        self.__courseId=id
        self.__courseName=name
        self.__sections=section
        self.__startDate=startDate
        self.__endDate=endDate
        self.__prerequisite=prerequisite
        self.__trainer=trainer
        self.__learners=learners

    def addCourse(self, id, name, startDate, endDate):
        # to check if the course start date is after the end date
        if startDate > endDate:
            raise Exception("Start date after end date, unable to add course")
        self.__courseId = id
        self.__courseName = name
        return self.__courseId

    def addTrainer(self, id, trainer):
        # to check if the trainer is already allocated to the course
        if id in trainer:
            return Exception("Course has already been allocated to trainer, unable to allocate")
        self.__trainer += trainer
        return self.__trainer

    def addLearner(self, id, learner, prerequisite):
        # to check if the prerequisite is met by the learner
        if prerequisite not in learner:
            return Exception("Prerequisite not met, unable to enroll")
        # to check if the learner has already enrolled/ completed the course
        if id in learner:
            return Exception("Course in progress/completed, unable to re-enroll")
        self.__learners += learner
        return self.__learners

    def viewSections(self):
        return(self.__sections)
    
    def viewCourse(self):
        return(self.__courseName)

