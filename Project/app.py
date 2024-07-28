from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase


app = Flask(__name__,
template_folder='templates',
static_folder='static')
app.config['SECRET_KEY'] = '*********78h6y5tfre5hgyu7yi'

firebaseConfig = {
  "apiKey": "AIzaSyDxaQjVOvNK3zIpQaozlVD2x1Yg5ytduKA",
  "authDomain": "amigo-journal-9f1a1.firebaseapp.com",
  "projectId": "amigo-journal-9f1a1",
  "storageBucket": "amigo-journal-9f1a1.appspot.com",
  "messagingSenderId": "628691355639",
  "appId": "1:628691355639:web:86c8dfd20c75f2875290f2",
  "measurementId": "G-LG19SXMM67",
  "databaseURL" : "https://amigo-journal-9f1a1-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


@app.route("/")
def hello ():
    return render_template("hello.html")

@app.route("/signup",methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form['name']  
        email = request.form['email']  
        password = request.form['password']  
        try:
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user["localId"]
            db.child("users").child(user_id).set()
            login_session['user'] = user
            return redirect(url_for('home'))

        except Exception as e :
            print(e)
            return "Failed to create account. Try again."
    return render_template('signup.html')


@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        try: 
            user = auth.sign_in_with_email_and_password(email, password)
            login_session['user']= user
            return redirect(url_for('home'))
        except:
            return "failed do something"
        
    return render_template('login.html')

        
        
@app.route("/home")
def home():
    user_id = login_session['user']["localId"]
    journals = db.child("journals").child(user_id).get().val()        

    return render_template("home.html",journals = journals )


@app.route("/journal" , methods = ["GET","POST"])
def journal():
    if request.method == "GET" :
        return render_template("journal.html")
    else:
        day = request.form['day']
        dh = request.form['highlight']
        challenges = request.form['victories']
        learned = request.form['learned']
        grateful = request.form['grateful']
        priority = request.form['priority']
        excited = request.form['excited']
        victories = request.form['victories']
        user = login_session['user']
        user_id = user["localId"]
        
        try:
            date = request.form['date']
            info = db.child("journals").child(user_id).push({
                "day": day,
                "date": date,
                "dh": dh,
                "challenges": challenges,
                "learned": learned,
                "grateful": grateful,
                "victories": victories,
                "priority": priority,
                "excited": excited, 
                })
        except:
             return "Failed to login. Check your credentials."
    return redirect(url_for('home'))

@app.route("/journal_show/<journal_id>")
def journal_show(journal_id):
    
    user_id = login_session['user']["localId"]
    journals = db.child("users").child(user_id).child(journal_id).get().val()

    return render_template("journal_info.html",journal=journal )

        

if __name__ == '__main__':
    app.run(debug=True,port = 5001)


    

