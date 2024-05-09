from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number=random.randint(1, 10)
    current_year=dt.datetime.now().year
    return render_template("index.html", randomNum=random_number, year=current_year)

@app.route('/guess/<name>')
def namewithrequest(name):
    parametros={
    "name":name
    }
    response=requests.get("https://api.genderize.io/", params=parametros)
    data=response.json()
    gender=data['gender']
    response1=requests.get("https://api.agify.io", params=parametros)
    data1=response1.json()
    age=data1["age"]
    return render_template("guess.html", userName= name, userGender=gender, userAge=age)

@app.route('/blog')
def get_blog():
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response=requests.get(blog_url)
    all_posts=response.json()
    return render_template("blog_project.html", posts=all_posts)

@app.route('/post/<num>')
def get_blog_by_id(num):
    print(num)
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response=requests.get(blog_url)
    data=response.json()
    selected_post=None
    for item in data:
        if item["id"]==int(num):
            selected_post=item
    print(selected_post)
    return render_template("post.html", post=selected_post)

if __name__ == "__main__":
    app.run(debug=True)

