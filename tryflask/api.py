from flask import Flask, render_template, url_for,redirect, Blueprint

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np, math, cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

api = Blueprint("api",__name__,static_folder = 'static', template_folder = 'templates')

flag = 0
fname = ""

classifier = Classifier("keras_model.h5","labels.txt")

labels = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"]
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@api.route('/', methods=['GET',"POST"])
@api.route('/home', methods=['GET',"POST"])
def home():
    global flag, fname
    flag = 0
    form = UploadFileForm()
    if form.validate_on_submit():
        flag = 1
        file = form.file.data # First grab the file
        file.filename = "Sign-image."+ file.filename.rsplit(".")[-1]
        #file.filename = "abc.jpeg"
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        fname = file.filename
        return render_template('index.html', flag = flag, form=form, fpath= 'static/'+fname)
    #form = UploadFileForm()
    return render_template('index.html', flag = flag, form=form)

def predict():
    # Load the model
    model = load_model('keras_model.h5')
    detector = HandDetector(maxHands=1)
    fpath = "tryflask/static/" + fname
    img = cv2.imread(fpath)
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgSize = 300
        offset = 20
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgCropShape = imgCrop.shape
    aspectRatio = h / w

    if aspectRatio > 1:
        k = imgSize / h
        wCal = math.ceil(k * w)
        imgResize = cv2.resize(imgCrop, (wCal, imgSize))
        imgResizeShape = imgResize.shape
        wGap = math.ceil((imgSize - wCal) / 2)
        imgWhite[:, wGap:wCal + wGap] = imgResize

    else:
        k = imgSize / w
        hCal = math.ceil(k * h)
        imgResize = cv2.resize(imgCrop, (imgSize, hCal))
        imgResizeShape = imgResize.shape
        hGap = math.ceil((imgSize - hCal) / 2)
        imgWhite[hGap:hCal + hGap, :] = imgResize
    prediction, index = classifier.getPrediction(imgWhite, draw=False)
    prediction = int(np.argmax(prediction))
    return labels[prediction]

@api.route('/answer')
def answer():
    if flag == 1:
        var = predict()
        return render_template('answer.html',text = var)
    else:
        return render_template('answer.html',text = "Please upload a file!")

#if __name__ == '__main__':
#    app.run(debug=True,port=8000)
