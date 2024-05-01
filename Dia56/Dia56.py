from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hola mundo</h1>"

@app.route("/Template")
def html():
    return render_template("index.html")

@app.route("/Movie")
def movie():
    return render_template("Dia43.html")

if __name__=="__main__":
    app.run(debug=True)


