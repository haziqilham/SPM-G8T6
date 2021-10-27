class Chapter():
    __chapter_id = 0
    __chapter_name = None
    __order = 0
    __chapter_materials = []

    def __init__(self, id, name, order, materials):
        self.__chapter_id = id
        self.__chapter_name = name
        self.__order = order
        self.__chapter_materials = materials

    #getter methods
    def getChapterId(self):
        return self.__chapter_id
    def getChapterName(self):
        return self.__chapter_name
    #order to determine which chapter comes first in the class
    def getOrder(self):
        return self.__order
    def getChapterMaterials(self):
        return self.__chapter_materials

    #setter methods
    def setChapterName(self, name):
        self.__chapter_name = name
        return self.__chapter_name
    def setOrder(self, order):
        self.__order = order
        return self.__order
    def setMaterial(self, material):
        self.__chapter_materials = material
        return self.__chapter_materials

    