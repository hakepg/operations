from flaskproj.flask_ui_designning.serviceimpl import *
from flask import request,render_template

servhotel = hotelservice()

@app.route('/service/',methods = ['GET'])
def welcome():
    return render_template('hotel.html')

@app.route('/saveform/',methods=['POST'])
def saveform():
    ht = Hotel(hotelid=request.form['hote_id'],
          hotelname=request.form['hotel_name'],
          hoteltype=request.form['hotel_type'])
    # ht.__dict__.pop('_sa_instance_state')
    print(ht.__dict__)
    servhotel.add_model(ht)
    # ht.__dict__.pop('_sa_instance_state')
    # print(ht.__dict__)
    return render_template('hotel.html')


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)