class Product:
    def __init__(self, pid, name):
        self.prodid = pid
        self.prodname = name
        

p = Product(pid=1, name='mob')
p1 = Product(pid=1, name='mob')

print(p.__dict__)
del p.prodid
print(p.__dict__)
print(p1.__dict__)