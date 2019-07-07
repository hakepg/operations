from flaskproj.flask_rest_api_p5batch.producer.prod_model import *
# db.create_all()
class prod_service:
    def add_prod(self,stud):
        db.session.add(stud)
        db.session.commit()
        db.session.remove()
        return 'student added successfully..'


    def get_prod(self,sid):
        return Student.query.filter_by(id=sid).first()


    def get_all_prod(self):
        return Student.query.all()


    def update_prod(self,stud):
        dbstud = self.get_prod(stud.id)
        if dbstud:
            dbstud.id = stud.id
            dbstud.name = stud.name
            dbstud.age = stud.age
            dbstud.city = stud.city
            db.session.commit()
            db.session.remove()
            return 'student updated successfully..'
        return 'student cannot found cannot added..'


    def delete_prod(self,sid):
        dbstud = self.get_prod(sid)
        if dbstud:
            db.session.delete(dbstud)
            db.session.commit()
            db.session.remove()
            return 'student deleted successfully..'
        return 'student record not found so cannot deleted..'
