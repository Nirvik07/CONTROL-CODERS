from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contactus'
db = SQLAlchemy(app)

class contacts(db.Model):
    uname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), primary_key=True)
    company = db.Column(db.String(100), nullable=True )


@app.route("/")

def home():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template('aboutus.html')

@app.route("/contact" , methods = ['GET', 'POST'])
def contact():
	if(request.method=='POST'):
		'''Fetch data and add it to the database'''
		uname = request.form.get('uname')
		email = request.form.get('email')
		company = request.form.get('company')
		print(uname, email, company)

		user = contacts(uname= uname, email = email, company= company)
		db.session.add(user)
		db.session.commit()
	return render_template('contactpage.html')

@app.route("/products")
def products():
	return render_template('products.html')

@app.route("/profile")
def profile():
	return render_template('profile.html')

app.run(debug=True)