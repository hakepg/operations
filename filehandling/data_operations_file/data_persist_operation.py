from abc import ABC,abstractmethod

class EmpOperation:

    @abstractmethod
    def write_into_text(self,data):
        pass

    @abstractmethod
    def read_from_text(self):
        pass

    @abstractmethod
    def write_into_file(self,data):
        pass

    @abstractmethod
    def read_from_file(self):
        pass

    @abstractmethod
    def write_into_db(self,data):
        pass

    @abstractmethod
    def read_from_db(self):
        pass
