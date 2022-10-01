# ----------------------------------------------------------------------------------------------------------------------

import face_recognition
import cv2
import os
import numpy as np
last_encoding = []
scale_percent = 50
# ----------------------------------------------------------------------------------------------------------------------

class FaceRecognition:

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    # ------------------------------------------------------------------------------------------------------------------
    def append_known_face_encoding(self, encoding):
        self.known_face_encodings.append(encoding)

    def append_known_face_names(self, name):
        self.known_face_names.append(name)

    # ------------------------------------------------------------------------------------------------------------------
    def load_encodings(self, name_encoding):
        for name, encoding in name_encoding:
            self.known_face_encodings.append (encoding)
            self.known_face_names.append (name)

    # ------------------------------------------------------------------------------------------------------------------

    def detect_known_faces(self, frame):
        # # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        name = ("Unknown", '')
        rgb_small_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_encodings = \
            face_recognition.face_encodings(rgb_small_frame, num_jitters=3,
                                            known_face_locations=[(0, frame.shape[1], frame.shape[0], 0)],
                                            model="large")
        face_distances = face_recognition.face_distance(self.known_face_encodings, face_encodings[0])
        if face_distances.size > 0:
            best_match_index = np.argmin(face_distances)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encodings[0], tolerance=0.5)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                if name == ("Unknown", ''):
                    return None
                return name
            else:
                self.known_face_encodings.append(face_encodings[0])
                self.known_face_names.append(("Unknown", ''))
                return ("Unknown", '')
        else:
            self.known_face_encodings.append(face_encodings[0])
            self.known_face_names.append(("Unknown", ''))
            return ("Unknown", '')

# ----------------------------------------------------------------------------------------------------------------------
