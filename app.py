from flask import Flask, render_template, url_for, redirect, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['Mail_SERVER'] = 'smtp.gmail.com'
app.config['Mail_PORT'] = 587
app.config['Mail_USE_TLS'] = True
app.config['Mail_USERNAME'] = '---email.gmail.com'
app.config['Mail_PASSWORD'] = 'yourpassword'

mail = Mail(app)


artworks = [
    {"title": "Africa", "price": 100.00, "description": "Portrait study inspired by a model from Pinterest.", "filename": "images/24_12_03.png"},
    {"title": "Landscape Study", "price": 220.50, "description": "Practice piece for an environmental scene.", "filename": "images/Landscape_Study.png"},
    {"title": "Liberian Girl", "price": 120.00, "description": "A portrait of a beautiful woman inspired from Pinterest.", "filename": "images/Liberian_girl.jpg"},
    {"title": "Light Study", "price": 200.00, "description": "Perspective practice", "filename": "images/Light_Study.png"},
    {"title": "Manga Pose", "price": 95.00, "description": "A piece where I was testing out manga styles.\nFrom my favorite artist Yusuke Murata.", "filename": "images/Manga_Pose.jpg"},
    {"title": "Portrait", "price": 100.00, "description": "A deep and contemplative portrait.", "filename": "images/Portrait.png"},
    {"title": "Riley x Cindy", "price": 150.00, "description": "Fan art from one of my favorite shows 'The Boondocks'.", "filename": "images/Riley_Cindy.jpg"}
]


def save_purchases(name, email, title):
    with open("purchases.txt", "a") as file:
        file.write(f"{name},{email},{title}")
        
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
                return redirect(url_for("thankyou"))
        else: 
            message = "Please fill in all fields"
        
    return render_template("index.html", artworks=artworks, message=message)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
    
# JSON file for artworks
# # styling (pep8 and Docstrings)
# Connect email 