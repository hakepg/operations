from abc import ABC,abstractmethod

class modelinfo(ABC):

    @abstractmethod
    def add_model(self,model):
        pass

    @abstractmethod
    def get_model(self,hid):
        pass

    @abstractmethod
    def get_all_info(self,model):
        pass

    @abstractmethod
    def update_model(self,model):
        pass

    @abstractmethod
    def delete_model(self,hid):
        pass
