from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
@app.route("/index")
@app.route('/home')
def home():
  return render_template("home.html", active_page= 'home')
@app.route("/about")
def getAbout():
  return render_template('about.html')

@app.route('/params')
def params():
  return request.args 

@app.route('/post_req', methods = ['POST'])
def post_req():
  return request.args  

@app.route("/contact")
def contact():
  return render_template('contact.html', phone = 87654321)  
app.run(host='0.0.0.0', port=8020, threaded=True, debug=True)

