from abc import ABC, abstractmethod

class Question(ABC):
    __question_id = 0
    __question = None
    __marks = 0

    def __init__(self, id, question, marks):
        self.__question_id = id
        self.__question = question
        self.__marks = marks
    
    #getter methods
    def getQuestion(self):
        return self.__question
    def getMarks(self):
        return self.__marks

    #settermethods
    def setQuestion(self, question):
        self.__question = question
        return self.__question
    def setMarks(self, marks):
        self.__marks = marks
        return self.__marks

    @abstractmethod
    def computemarks(self):
        pass