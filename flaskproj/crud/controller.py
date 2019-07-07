from flaskproj.crud.dbconfig import app,db
from flask import render_template,request
from flaskproj.crud.serviceimplinfo import prodservimpl
impl=prodservimpl()
from flaskproj.crud.modelinfo import Product

app.route('/')
def product():
    # listofproduct=impl.get_all_prod()
    # return render_template('productinfo.html',prodlist=listofproduct)
    return 'hello'

# def saveproduct():
#     print(request.form)
#     prod=Product(request.form('id'),request.form('name'),request.form('price'),request.form('quantity'),request.form('category'))
#     impl.add_prod(prod)
#     listofproduct=impl.get_all_prod()
#     return render_template('productinfo.html',prodlist=listofproduct)



if __name__=='__main__':
    app.run(debug=True,port=5002)