from flask import Flask, render_template, flash,redirect,url_for,request,session
from flask_bcrypt import generate_password_hash, check_password_hash
from database import User

app = Flask(__name__)
app.secret_key = "jhdfgfggafrgfhxh"


@app.route('/')
def home():  # put application's code here
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template('home.html')


@app.route('/register', methods = ['GET','POST'])
def register():  # put application's code here
    if request.method == "POST":
        jina = request.form["u_name"]
        arafa = request.form["u_email"]
        siri = request.form["u_pass"]
        siri = generate_password_hash(siri)
        User.create(name = jina, email = arafa, password = siri)
        flash("registration successful")
    return render_template("register.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():  # put application's code here
    if request.method == "POST":
        email = request.form["u_email"]
        password = request.form["u_pass"]
        try:
            user = User.get(User.email == email)
            hashed_password = user.password
            if check_password_hash(hashed_password,password):
                flash("login successful")
                session["logged_in"] = True
                session["name"] = user.name
                return redirect(url_for("home"))
            else:
                flash("wrong email or password")
        except:
            flash("operation is not permited at this time")
    return render_template("login.html")


    return render_template("login.html")


if __name__ == '__main__':
    app.run()
