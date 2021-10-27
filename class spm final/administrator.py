from user import User

class Administrator(User):
    def __init__(self, id, username, name, designation, department, role):
        User.__init__(self,id, username, name, designation, department, role)
    def enroll(self):
        pass
