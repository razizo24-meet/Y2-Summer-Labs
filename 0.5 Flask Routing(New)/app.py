from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return("<html> <p> welcome to our surfing gallary </p> <br> <a href ='/photo 1 /<html>")
    
    @app.route('/photo 1')
    def photo 1():
        return('<html> <img> source = " 4E892F73-D6B7-4A81-BF0D-C39A6396B76B_1_105_c" </img></html>')
        
    
if __name__ == '__main__':
    app.run(debug=True)