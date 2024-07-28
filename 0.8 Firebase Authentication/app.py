from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase
 
app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = '*********'

firebaseConfig = {
    "apiKey": "AIzaSyCkRZ8O9agl4aP3L2GvagYtf06XhTlHsKM",
    "authDomain": "first-project-auth-8f621.firebaseapp.com",
    "databaseURL": "https://first-project-auth-8f621.firebaseio.com",
    "projectId": "first-project-auth-8f621",
    "storageBucket": "first-project-auth-8f621.appspot.com",
    "messagingSenderId": "543324356799",
    "appId": "1:543324356799:web:63376431f93daad635460a",
    "measurementId": "G-XZ5BH9FRJL",
    "databaseURL" : "https://first-project-auth-8f621-default-rtdb.europe-west1.firebasedatabase.app/"
    
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form['email']
        password = request.form['password']
        
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "There is something wrong."
            return render_template("login.html", error=error)
        
        

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            login_session['quotes'] = [] 
            yo = login_session['quotes'] 
            return redirect(url_for('home'))
        except:
            error = "Signup failed. Please try again."
            return render_template("signup.html", error=error)
        

@app.route('/signout')
def signout():
    login_session.pop('user', None)
    print("signed out user")
    return redirect(url_for('login'))



@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' in login_session:
        if request.method == "POST":
            quote = request.form['quote']
            try:
                login_session["quotes"].append(quote)
                login_session.modified = True
                print(quote)
            except:
                print("error")
            return redirect(url_for("thanks"))
        return render_template("home.html")
    else:
        return redirect(url_for('login'))
    
    

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")



@app.route('/display')
def display():
    yo = login_session['quotes'] 
    return render_template("display.html",yo = yo)



if __name__ == "__main__":
    app.run(debug=True)