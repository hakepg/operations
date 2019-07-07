
class Product:

    def __init__(self,pid,pname,pprice,pvendor,pcatogry):
        self.prodId=pid
        self.prodName=pname
        self.prodPrice=pprice
        self.prodVend=pvendor
        self.prodCat=pcatogry


    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)

# prod=Product(pid=1,pname='mob',pprice=25468,pvendor='flip',pcatogry='A')
# print(prod)