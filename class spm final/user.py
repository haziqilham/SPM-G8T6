class User():

    __user_id = 0
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

    #Getter Methods
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

    #Setter Methods
    def setUserName(self, username):
        self.__user_name = username
        return self.__user_name
    def getName(self, name):
        self.__name = name
        return self.__name
    def getDesignation(self, designation):
        self.__designation = designation
        return self.__designation
    def getDepartment(self, department):
        self.__department = department
        return self.__department
    def getRole(self, role):
        self.__role = role
        return self.__role


    def enroll(self):
        #check capacity, check course, check course prereqs
        pass

