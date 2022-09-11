from flask import Flask, render_template, Response, jsonify
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from .camera import VideoCamera
import webbrowser, os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

camera = VideoCamera()

@app.route('/')
def index():
    return render_template('about.html')

def gen():

    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
     return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/main')
def home():
    return render_template('home.html')
    

@app.route('/faq')
def faq():
    return render_template('faq.html')


#app.jinja_env.globals.update(delete=delete)
#app.jinja_env.globals.update(init_cam=init_cam)
