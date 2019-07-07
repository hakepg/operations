from flaskproj.crud.dbconfig import db

class Product(db.Model):
    prodId=db.Column(db.Integer,primary_key=True)
    prodName=db.Column(db.String(50),nullable=False)
    prodPrice=db.Column(db.Float(50))
    prodQty=db.Column(db.Integer)
    prodCategory=db.Column(db.String(50))

    def __str__(self):
        return f'{self.prodId, self.prodName,self.prodPrice,self.prodQty,self.prodCategory}'

    def __repr__(self):
        return str(self)

# p1=Product(prodId=1,prodName='mob',prodPrice=4525,prodQty=3,prodCategory='accessories')
# p2=Product(prodId=2,prodName='iphone',prodPrice=45255,prodQty=2,prodCategory='accessories')
# p3=Product(prodId=3,prodName='notepad',prodPrice=35265,prodQty=6,prodCategory='accessories')
# p4=Product(prodId=4,prodName='ipad',prodPrice=8525,prodQty=7,prodCategory='accessories')
# p5=Product(prodId=5,prodName='bluetooth',prodPrice=525,prodQty=3,prodCategory='accessories')
# print(p1)

# db.create_all() #only table is created
# db.drop_all() #drop all the tables
# db.session.add()#add one by one entity
# db.session.add_all([p1,p2,p3,p4,p5]) #add all the entity at a time
# db.session.commit()# save the data into ur database..after adding data commit is compulsary to save

