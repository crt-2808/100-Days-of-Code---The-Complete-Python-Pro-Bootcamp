from flask import Flask, render_template, request
import smtplib

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def recived_data():
    name=request.form["name"]
    passw=request.form["password"]
    return f"<h1>Name: {name}, Pass: {passw}</h1>"

if __name__=="__main__":
    app.run(debug=True)

