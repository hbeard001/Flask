from flask import Flask

app=Flask(__name__)
@app.route("/")
def homepage():
    return "<h1>Welcome to my homepage </h1>"
@app.route("/aboutus")
def message():
    return "<B> Hello</b> <u>my friends</u>"

@app.route("/nbs")
def boom():
    return "Welcome to NBS"
app.run()