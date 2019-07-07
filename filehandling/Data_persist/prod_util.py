from filehandling.Data_persist.prodinfo import Product
import random
def generate_random_name():
    name=''
    for item in range(0,random.randint(5,12)):
        randno=random.randint(65,90)
        name+=chr(randno)
    return name

def generate_product(count):
    listofproducts=[]
    for prod in range(count):

        p1=Product(pid=random.randint(111,999),pname=generate_random_name(),
                   pprice=round(random.randint(1111,9999/3,3)),
                   pvendor=generate_random_name(),pcatogry='A')
        listofproducts.append(p1)
    return listofproducts
