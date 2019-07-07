from abc import ABC,abstractmethod

class ModelService(ABC):

    @abstractmethod
    def createModel(self):
        pass

    @abstractmethod
    def getModel(self):
        pass

    @abstractmethod
    def getAllModel(self):
        pass

    @abstractmethod
    def updateModel(self):
        pass

    @abstractmethod
    def deleteModel(self):
        pass

