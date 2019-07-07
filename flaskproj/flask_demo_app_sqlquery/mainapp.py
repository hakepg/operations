from flask import Flask,request,render_template
from flaskproj.flask_demo_app_sqlquery.empinfo import Employee
from flaskproj.flask_demo_app_sqlquery.db_query import create_employee_records, get_all_empinfo
app = Flask(__name__)

@app.route('/welcome/',methods=["GET"])
def landing_page1():
    return 'hello python'

@app.route('/index/',methods = ['POST','GET'])
def student_page():
    emp = Employee(eid=request.form['empid'],
                   ename=request.form['empname'],
                   eage=request.form['empage'],
                   esal=request.form['empsalary'])
    print(emp)
    create_employee_records(emp)
    return render_template('emp.html',employees=get_all_empinfo())

@app.route("/home")
def landing_page2():
    return render_template('emp.html',employess=get_all_empinfo())



if __name__ == '__main__':
    app.run(debug=True)