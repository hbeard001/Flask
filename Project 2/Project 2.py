from flask import Flask, render_template,request,redirect
import mysql.connector

app=Flask(__name__)
db=mysql.connector.connect(host="localhost",
                           user="root",
                           password="root",
                           database="mis2"
                           )
mycursor=db.cursor()

@app.route("/")
def homePage():
       return render_template("inputformDept.html")

@app.route("/ShowRecords",methods=["post"])
def Showrecords():
    dept=request.form["dept"]
    mycursor.execute("select * from personal where department='"+dept+"'")
    records=mycursor.fetchall();

    return render_template("ListofRecords.html",data=records)

@app.route("/payslip/<empno>")
def payslip(empno):
    mycursor.execute("Select * from personal where empno="+empno)
    personalrecords=mycursor.fetchall();
    mycursor.execute("Select * from accounts where empno="+empno)
    salaryrecords=mycursor.fetchall()
    return render_template("payslip.html",personal=personalrecords,accounts=salaryrecords)
       


@app.route("/saverecord",methods=["post"])
def saverecord():
    salary=request.form["salary"]
    empno=request.form["empno"]
    sql1="insert into accounts(empno,salaryDate,amount) values('{0}',now(),'{1}')".format(empno,salary)
    mycursor.execute(sql1)
    db.commit()
    return redirect("/")

app.run(debug=True)    
    