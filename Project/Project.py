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
    mycursor.execute("Select * from personal")
    records=mycursor.fetchall();

    return render_template("HomePage.html",data=records)

@app.route("/departments/<dept>")
def departmentlist(dept):
    mycursor.execute("select * from personal where departments='"+dept+"'")
    records=mycursor.fetchall();

    return render_template("HomePage.html",data=records)

@app.route("/newrecord")
def newrecord():
    return render_template("inputform.html")

@app.route("/saverecord",methods=["post"])
def saverecord():
    name=request.form["na"]
    dept=request.form["dept"]
    sql1="insert into personal(name,department) values('{0}','{1}')".format(name,dept)
    mycursor.execute(sql1)
    db.commit()
    return redirect("/")

@app.route("/details/<empno>")
def details(empno):
    mycursor.execute("Select * from personal where empno="+empno)
    personalrecords=mycursor.fetchall();
    mycursor.execute("Select * from personal where empno="+empno)
    salaryrecords=mycursor.fetchall()
    return render_template("details.html",personal=personalrecords,acconts=salaryrecords)

app.run(debug=True)    
    