# ----------------------------------------------------------------------------------------------------------------------

import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2 as cv2
from concurrent.futures import ThreadPoolExecutor
from controller.FaceRecognition import FaceRecognition

# ----------------------------------------------------------------------------------------------------------------------

prototxtPath = "face_detector/deploy.prototxt"
weightsPath = "face_detector/res10_300x300_ssd_iter_140000.caffemodel"
maskNet = load_model("./controller/mask_detector.model")
FacesImagesFolder = r"savedImages/Faces"
FullImagesFolder = r"savedImages/FullImages"

# thread_pool = ThreadPoolExecutor(max_workers=1)
# sfr = FaceRecognition()
# sfr.load_encodings()
# sfr.load_encoding_images("controller/images")

# ---------------------
mouth_cascade = cv2.CascadeClassifier('./controller/cascades/haarcascade_mcs_mouth.xml')
"""nose_cascade = cv2.CascadeClassifier('./controller/cascades/haarcascade_mcs_nose.xml')"""


# ----------------------------------------------------------------------------------------------------------------------

def detect_and_predict_mask(frame, faceNet, maskNet):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (400, 400),
                                 (124.96, 115.97, 106.13))

    faceNet.setInput(blob)
    detections = faceNet.forward()

    faces = []
    locs = []
    preds = []

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            face = frame[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)

            faces.append(face)
            locs.append((startX, startY, endX, endY))

    if len(faces) > 0:
        faces = np.array(faces, dtype="float32")
        preds = maskNet.predict(faces, batch_size=11)

    return (locs, preds)


# ----------------------------------------------------------------------------------------------------------------------

def getFrame(sfr: FaceRecognition, thread_pool, frame, counter, q, threadLock):
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

    # frame = imutils.resize(frame, width=400)
    frame = cv2.flip(frame, 1)
    (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

    for (box, pred) in zip(locs, preds):
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred

        label = "No Mask" if mask > withoutMask else "Mask"
        color = (0, 0, 255) if label == "No Mask" else (0, 255, 0)

        # ---------------
        # TODO: change!!, just for checking
        if label == "Mask":
            if mouth_detected(frame[startY+20:endY+20, startX+20:endX+20]):
                label = "No Mask"
                color = (0, 0, 255)
        # ---------------

        if label == "No Mask" and counter % 2 == 0:
            # making a thread for face recognition
            thread_pool.submit(run_rec, sfr, frame[startY:endY, startX:endX], q, threadLock)

        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        cv2.putText(frame, label, (startX, startY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
    return frame


# ----------------------------------------------------------------------------------------------------------------------

def run_rec(sfr, frame, q, thread_lock):
    face_name = sfr.detect_known_faces(frame)
    print(face_name)
    if face_name is None:
        return
    try:
        thread_lock.acquire()
        q.put((frame, face_name))
        thread_lock.release()
    except:
        print("thread error")


# ----------------------------------------------------------------------------------------------------------------------

def mouth_detected(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
    return len(mouth_rects) != 0


"""def nose_detected(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    nose_rects = nose_cascade.detectMultiScale(gray, 1.7, 11)
    return len(nose_rects) != 0"""
