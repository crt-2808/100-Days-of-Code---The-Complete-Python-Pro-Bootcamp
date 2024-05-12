from flask import Flask, render_template, request
import requests
import os
import dotenv
import smtplib

dotenv.load_dotenv()

myEmail=os.getenv("SMTP_MAIL")
myPassword=os.getenv("SMTP_PASSWORD")
post=requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_posts=post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method=="POST":
        data=request.form
        send_email(name=data["name"], email=data["email"], phone=data["phone"], message=data["message"])
        return render_template("contact.html", message_sent=True)

    return render_template("contact.html", message_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post=None
    for blog_post in post:
        if blog_post["id"]==index:
            requested_post=blog_post
    return render_template("post.html", post=requested_post)

def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(myEmail, myPassword)
        connection.sendmail(from_addr=myEmail,
                            to_addrs=myEmail,
                            msg=f"Subject:New Message!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")

if __name__=="__main__":
    app.run(debug=True)