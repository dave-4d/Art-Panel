from flask import Flask, render_template, url_for, redirect, request
from flask_mail import Mail, Message
import json


app = Flask(__name__)

# email configuration (Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rubgdavid@gmail.com'
app.config['MAIL_PASSWORD'] = 'vodx pwia srsv zljx'

mail = Mail(app)

# Load artworks data from JSON file
with open("artworks_data.json", "r") as f:
    artworks = json.load(f)


# This saves the purchase purchasing info 
def save_purchases(name, email, title):
    with open("purchases.txt", "a") as file:
        file.write(f"{name},{email},{title}")
        
# This sends an email. A small receipt for the purchase
def send_purchases_email(recipient, art):
    subject = f"Thanks for Purchasing: {art['title']}"
    body = f"""Hi,
    
Thanks for supporting me by purchasing "{art['title']}😊

Description: {art['description']}

Price: {art['title']}

I appreciate your Support!
"""
    msg = Message(subject, recipients=[recipient], body=body, sender=app.config['MAIL_USERNAME'])
    mail.send(msg)
        
        
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    
    if request.method == "POST":
        name= request.form.get("name")
        email= request.form.get("email")
        title= request.form.get("title")
        
        if name and email and title:
            found = False
            for art in artworks:
                if art["title"] == title:
                    found = True
                    break
            
            if found:
                save_purchases(name, email, title)
                art = next((a for a in artworks if a["title"] == title), None)
                if art:
                    send_purchases_email(email, art)
                return redirect(url_for("thankyou"))
        else: 
            message = "Please fill in all fields"
        
    return render_template("index.html", artworks=artworks, message=message)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
