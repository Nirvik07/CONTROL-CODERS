from flask import flash, session
# from gevent.pywsgi import WSGIServer
from tabnanny import check
from unicodedata import category
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
import sqlite3
import time
import datetime
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/contactus'
app.secret_key = b'\xe6C\xf3Md\xaa\xcf\x15\xda\xa3\xf0\x95'
db = SQLAlchemy(app)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactus'
app.config['MySQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


class contacts(db.Model):
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), primary_key=True)
    Subject = db.Column(db.String(100), nullable=False)
    Message = db.Column(db.String(500), nullable=False)


class user(db.Model):
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), primary_key=True)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('aboutus.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        '''Fetch data and add it to the database'''
        uname = request.form.get('name')
        email = request.form.get('email')
        Subject = request.form.get('subject')
        Message = request.form.get('message')
        print(uname,email,Subject,Message)
        account = contacts(name=uname, email=email, Subject=Subject, Message=Message)
        db.session.add(account)
        db.session.commit()
    return render_template('contactpage.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        '''Fetch data and add it to the database'''
        username = request.form.get('Username')
        email = request.form.get('email')
        password = request.form.get('password')
        rpassword = request.form.get('repassword')
        if password != rpassword:
            print('Error')
        else:
            print(username, email, password)
            users = user(username=username, email=email, password=password)
            db.session.add(users)
            db.session.commit()
    return render_template('register.html')


# def register():
#     msg = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
#         account = cursor.fetchone()
#         if account:
#             msg = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address !'
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             msg = 'Username must contain only characters and numbers !'
#         elif not username or not password or not email:
#             msg = 'Please fill out the form !'
#         else:
#             cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
#             mysql.connection.commit()
#             msg = 'You have successfully registered !'
#     elif request.method == 'POST':
#         msg = 'Please fill out the form !'
#     return render_template('register.html', msg = msg)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if (request.method == 'GET'):
         return render_template('login.html')
    if (request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('password')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql_query = "SELECT * FROM user where email = '{}' and password = '{}'"
        sql_query = sql_query.format(email, password)
        cursor.execute(sql_query)
        record = cursor.fetchone()
        if not record:
            flash('Incorrect password', category='error')

        else:
            flash('Logged In Successfully', category='success')
            return render_template('profile.html', record=record)
        # uname = user.query.filter_by(email=email).first()
        # if uname:
        #     if password == cursor.fetchone():
        #         flash("Logged in Successfully")
        #     else:
        #         flash('Incorrect password', category='error')
        # else:
        #     flash('Email Does Not Exist', category='error')


@app.route("/products")
def products():
    return render_template('products.html')


@app.route("/profile")
def profile():
    global r
    return render_template('profile.html', record=r)


@app.route("/cart")
def cart():
    
    return render_template("cart.html",)
    # imageList = os.listdir('CONTROL-CODERS-main/InfinityStore/static/assets/images')
    # imagesList = ['images' + image for image in imageList]
    # return render_template("cart.html", imageList=imageList)

@app.route("/item1")
def item1():
    if (request.method == 'GET'):
         return render_template('item1.html')
    if (request.method == 'POST'):
        return render_template('cart.html')

@app.route("/item2")
def item2():
    return render_template('item2.html')

@app.route("/item3")
def item3():
    return render_template('item3.html')

@app.route("/item4")
def item4():
    return render_template('item4.html')

@app.route("/item5")
def item5():
    return render_template('item5.html')

@app.route("/item6")
def item6():
    return render_template('item6.html')

@app.route("/item7")
def item7():
    return render_template('item7.html')

@app.route("/item8")
def item8():
    return render_template('item8.html')

@app.route("/item9")
def item9():
    return render_template('item9.html')

@app.route("/item10")
def item10():
    return render_template('item10.html')

@app.route("/item11")
def item11():
    return render_template('item11.html')

@app.route("/item12")
def item12():
    return render_template('item12.html')

@app.route("/item13")
def item13():
    return render_template('item13.html')

app.run(debug=True)


