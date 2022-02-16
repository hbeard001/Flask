from flask import Flask

app=Flask(__name__)
@app.route("/")
def homepage():
    return """
            <html>
            <center><h1>Welcome to my homepage </h1></center>
            We are the only building society in the UK<br>
            <a href="http://localhost:5000/Team"> Who we are </a> <br>
            <a href="http://localhost:5000/Services"> Our services </a> <br>
           </HTML>
            """
@app.route("/Team")
def message():
    return """
        <html>
        <h1> Out team members are </h1>
        <br>
        Haydn <br>
        Lee<br>
        Baboucarr<br>
        Louise<br>
        Mimi<br>
        Stewart<br>
        Sophie<br>
        George<br>
        Darryn<br>
        Laura<br>
        Marianne<br>
        Sarah<br>
        Seth<br>
        Sophie<br>
        <br>
        <a href="http://localhost:5000"> Home </a>
        <br>
        """

@app.route("/Services")
def boom():
    return """
        <html>
        <h2> <center> We provide the following services </center></h2>
        <br>
        <a href="http://localhost:5000"> Home </a>
        <br>
        <ul>
            <li> Open Account</li>
            <li> Deposit Money</li>
            <li> Withdraw money </i>
        </ul>
        </html>
    """
app.run()