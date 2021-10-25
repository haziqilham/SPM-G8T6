class User():

    __user_id = None
    __user_name = None
    __name = None
    __designation = None
    __department = None
    __role = None

    def __init__(self, id, username, name, designation, department, role):
        self.__user_id = id
        self.__user_name = username
        self.__name = name
        self.__designation = designation
        self.__department = department
        self.__role = role

    def getId(self):
        return self.__user_id
    def getUserName(self):
        return self.__user_name
    def getName(self):
        return self.__name
    def getDesignation(self):
        return self.__designation
    def getDepartment(self):
        return self.__department
    def getRole(self):
        return self.__role
    

class Administrator(User):
    def __init__(self, id, username, name, designation, department, role):
        User.__init__(self,id, username, name, designation, department, role)
    
    def createCourse(self):
        pass
    def createClass(self):
        pass
    def enrollLearners(self):
        pass


class Learners(User):
    def __init__(self, id, username, name, designation, department, role):
        User.__init__(self,id, username, name, designation, department, role)
    
    def enrollClass(self):
        pass

class Trainers(User):
    def __init__(self, id, username, name, designation, department, role):
        User.__init__(self,id, username, name, designation, department, role)
    
    def createQuiz(self):
        pass