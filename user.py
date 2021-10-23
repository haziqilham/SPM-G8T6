class User():

    __userId = None
    __name = None
    __designation = None
    __department = None
    __role = None

    def __init__(self, id, name, designation, department, role):
        self.__userId = id
        self.__name = name
        self.__designation = designation
        self.__department = department
        self.__role = role

    def getId(self):
        return self.__userId
    def getName(self):
        return self.__name
    def getDesignation(self):
        return self.__designation
    def getDepartment(self):
        return self.__department
    def getRole(self):
        return self.__role
    

class Administrator(User):
    def __init__(self, id, name, designation, department, role):
        User.__init__(self,id, name, designation, department, role)


class Learners(User):
    def __init__(self, id, name, designation, department, role):
        User.__init__(self,id, name, designation, department, role)

class Trainers(User):
    def __init__(self, id, name, designation, department, role):
        User.__init__(self,id, name, designation, department, role)