from flask import Flask,render_template

app=Flask(__name__)
@app.route("/info1")
def homepage1():
    return render_template("information.html",na="Haydn",addr="Bristol",color="red")    
    
@app.route("/info2")
def homepage2():
    return render_template("information.html",na="Haydn",addr="Bristol",color="green")    

@app.route("/info3")
def homepage3():
    return render_template("information.html",na="Haydn",addr="Bristol",color="yellow")        

app.run()