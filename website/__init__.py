from flask import Flask, render_template, Response, jsonify
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from .camera import VideoCamera
import webbrowser, os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'


def init_cam():
    print("Initiating camera")
    global camera
    camera = VideoCamera()
def delete_cam():
    print("Deleting camera")
    global camera
    del camera
    camera = None

def toggle_camera():
    if camera is None:
        init_cam()
    else:
        delete_cam()

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

app.jinja_env.globals.update(delete_cam=delete_cam)
app.jinja_env.globals.update(init_cam=init_cam)
