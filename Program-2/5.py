from flask import Flask,render_template

app=Flask(__name__)
@app.route("/salaryslip1")
def homepage1():
    name1="Haydn"
    salary1=15000
    return render_template("SalarySlip.html",name=name1,salary=salary1)    

app.run()