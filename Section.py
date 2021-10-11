#managed by Xinyi Pang

class Section:
    __sectionId=0
    __sectionName=None
    __material=None

    def __init__(self, id, nm, mat):
        self.__sectionId=id
        self.__sectionName=nm
        self.__material=mat

    def id(self):
        return (self.__sectionId)

    def name(self):
        return (self.__sectionName)

    def material(self):
        return (self.__material)

    def addMaterial(self, material):
        self.__material += material
        return self.__material

    def deleteMaterial(self, material):
        self.__material = None
        return self.__material