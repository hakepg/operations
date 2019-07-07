from flaskproj.flask_ui_designning.model import *
from flaskproj.flask_ui_designning.serviceinfo import *


class hotelservice(modelinfo):
    def add_model(self,model):
        if type(model) in [Hotel,Address]:
            db.session.add(model)
            db.session.commit()
            db.session.remove()
            return 'model added successfully..'

    def get_model(self,hid,ty):
        returnmodel=None
        if ty == Hotel:
            returnmodel = Hotel.query.filter_by(hid=hid).first()
        elif ty == Address:
            returnmodel = Address.query.filter_by(aid=hid).first()
        return returnmodel



    def get_all_model(self,model):
        returnmodel = None
        if model == Hotel:
            returnmodel = Hotel.query.all()
        elif model == Address:
            returnmodel = Address.query.all()
        return returnmodel


    def update_model(self,model):
        dbmodel = self.get_model(hid=model.id,ty=type(model))
        if type(model)== Hotel:
            dbmodel.hname = model.hname
            dbmodel.htype = model.htype
            db.session.commit()
        elif type(model) == Address:
            dbmodel.pin = model.pin
            dbmodel.city = model.city
            dbmodel.hot_id = model.hot_id
            db.session.commit()
            db.session.remove()


    def delete_model(self,hid,model):
        dbmodel = self.get_model(hid=hid,ty = model)
        db.session.delete(dbmodel)
        db.session.commit()
        db.session.remove()



# db.drop_all()
db.create_all()
