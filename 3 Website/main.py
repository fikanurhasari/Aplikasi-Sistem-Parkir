from flask import Flask,jsonify,request,render_template,redirect,url_for, make_response, session, flash
from flask_restx import Resource, Api,reqparse
from flask_mysqldb import MySQL, MySQLdb
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.datastructures import FileStorage
from keras.models import load_model
import keras_preprocessing
from keras_preprocessing import image
from keras.utils import load_img, img_to_array
import cv2
import bcrypt
import numpy as np
from matplotlib import pyplot as plt
import os
import tensorflow as tf
from tensorflow import keras
import chatbot
import easyocr
from keras.preprocessing import image
from PIL import Image as im

app = Flask(__name__)
api = Api(app)
CORS(app)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///images.db"
db.init_app(app)

#tabel image
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    plat = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False)
    
with app.app_context():
        db.create_all()







@api.route('/image/all', methods=["GET"])
class ImageAll(Resource):
    def get(self):
        images = db.session.execute(db.select(Image).order_by(Image.id)).scalars()
        data = []
        for image in images:
            data.append({
               'id': image.id,
                'name': image.name,
                'plat': image.plat,
                'created_at': image.created_at,

                       })
        return (data)

from werkzeug.datastructures import FileStorage
uploadParser = api.parser()
uploadParser.add_argument('image', location='files', type=FileStorage, required=True)
@api.route('/image')
class ImageAPI(Resource):
    @api.expect(uploadParser)
    def post(self):
        args = uploadParser.parse_args()
        file = args['image']
        file.save("./file_images/" + file.filename)
        filename = file.filename
        today = datetime.today()
        tanggal = f'{today}'
        
        #AI MODEL
        model = load_model('best-model.h5')
        path = "./file_images/" + filename
        img = cv2.resize(cv2.imread(path)/255.0, dsize=(224, 224))
        img_=cv2.imread(path)
        WIDTH = img.shape[1]
        HEIGHT = img.shape[0]
        y_hat = model.predict(img.reshape(1,WIDTH,HEIGHT,3)).reshape(-1)
    
        top_x, 	top_y = int(y_hat[0]),int(y_hat[1])
        bottom_x, bottom_y = int(y_hat[2]),int(y_hat[3])
        
        cropped_img=img_[424-10:611+10,289-1:678+10]
        # 289 678 424 611
        imgg = im.fromarray(cropped_img)
        print(top_x,bottom_x,top_y,bottom_y)
        
        reader=easyocr.Reader(['en'])

        
        output = reader.readtext(cropped_img, detail=0)
        plat = output[0]
        image = Image(name=filename, plat=plat, created_at=tanggal)
        db.session.add(image)
        db.session.commit()
        return jsonify({"no_plat": plat , 
                        "created_at" : tanggal,})

chatbotParser = reqparse.RequestParser()
chatbotParser.add_argument('msg', type=str, help='Message', location='args')
@api.route('/getchatbot')
class Chatbot(Resource):
    @api.expect(chatbotParser)
    def get(self):
        args = chatbotParser.parse_args()
        msg = args['msg']
        return chatbot.chatbot_response(msg)


app.secret_key = "membuatLOginFlask1"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'uasparkirdb'
app.config['MYSQL_PORT'] = 3308
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def main() :
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = curl.fetchone()
        curl.close()

        if user is not None and len(user) > 0 :
            if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
                session['name'] = user ['name']
                session['email'] = user['email']
                return redirect(url_for('home'))
            else :
                flash("Gagal, Email dan Password Tidak Cocok")
                return redirect(url_for('login'))
        else :
            flash("Gagal, User Tidak Ditemukan")
            return redirect(url_for('login'))
    else: 
        return render_template("login.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else :
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)" ,(name, email, hash_password)) 
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/history')
def history():
    images = Image.query.all()
    return render_template('histori.html', images=images)

@app.route('/chats')
def chats():
    return render_template('chats.html')





if __name__ == '__main__':
    app.run(host='192.168.43.233', port=5000, debug=True)