from abc import ABC,abstractmethod

class serviceprod(ABC):

    @abstractmethod
    def add_prod(self,prod):
        pass


    @abstractmethod
    def get_prod(self,pid):
        pass


    @abstractmethod
    def update_prod(self,prod):
        pass


    @abstractmethod
    def delete_prod(self,pid):
        pass


    @abstractmethod
    def get_all_prod(self):
        pass