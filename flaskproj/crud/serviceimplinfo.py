from flaskproj.crud.serviceinfo import serviceprod
from flaskproj.crud.modelinfo import Product
from flaskproj.crud.dbconfig import db

class prodservimpl(serviceprod):

    def add_prod(self, prod):
        dbprod= self.get_prod(prod.prodId)
        if dbprod:
            print('Product already exist')
        else:
            db.session.add(prod)
            db.session.commit()
            print('product added successfuly')



    def get_prod(self, pid):
        return Product.query.filter_by(prodID=pid).first()



    def update_prod(self, prod):
        dbprod=self.get_prod(prod.prodId)
        if dbprod:
            dbprod.prodName=db.prodName
            dbprod.prodPrice=db.prodPrice
            dbprod.prodQty=db.prodQty
            dbprod.prodCategory=db.prodCategory
            db.session.commit()
            print('product updated successfully')




    def delete_prod(self, pid):
        dbprod=self.get_prod(pid)
        if dbprod:
            db.session.delete(dbprod)
            db.session.commit()
            print('product deleted successfully..!')
        else:
            print('product cannot found..')



    def get_all_prod(self):
        return Product.query.all()