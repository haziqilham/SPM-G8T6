from user import User

class Trainers(User):
    def __init__(self, id, username, name, designation, department, role):
        User.__init__(self,id, username, name, designation, department, role)