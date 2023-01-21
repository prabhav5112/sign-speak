import numpy as np, mediapipe as mp, math, cv2, os, time
from tensorflow.python.keras.models import load_model
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from deepface import DeepFace

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf

detector = HandDetector(maxHands=1)
classifier = Classifier("keras_model.h5", "labels.txt")
offset = 20
imgSize = 300
labels = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"]
val = "happy"

class VideoCamera():
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global val
        success, img = self.video.read()
        imgOutput = img.copy()
        try:
            result = DeepFace.analyze(imgOutput,actions=['emotion'])
            if result['dominant_emotion'] != val:
                val = result['dominant_emotion']
        except:
            pass
        cv2.putText(imgOutput, val, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        hands, img = detector.findHands(img)
        if hands and hands[0]['bbox'][0] >= 50 and hands[0]['bbox'][1] >= 50:
            hand = hands[0]
            x, y, w, h = hand['bbox']   	
            if x <= offset + 10 or y <= offset + 10:
                imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            else:
                imgCrop = img[y:y + h + offset, x:x + w + offset]
            imgSymbol = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            imgCropShape = imgCrop.shape

            aspectRatio = h / w

            if aspectRatio > 1 and imgCrop is not None:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgSymbol[:, wGap:wCal + wGap] = imgResize

            elif imgCrop is not None and aspectRatio < 1:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgSymbol[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgSymbol, draw=False)
            cv2.rectangle(imgOutput, (x - offset, y - offset - 50), (x - offset + 90, y - offset - 50 + 50),(11, 133, 21), cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (11, 133, 21), 4)

        ret, jpeg = cv2.imencode('.jpg', imgOutput)

        return jpeg.tobytes()
