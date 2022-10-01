# ----------------------------------------------------------------------------------------------------------------------

import cv2
from PySide6.QtCore import *

import numpy as np
from controller.FaceMaskDetection import getFrame


# ----------------------------------------------------------------------------------------------------------------------

class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, q, threadLock, sfr, thread_pool):
        super().__init__()
        self.q = q
        self._run_flag = True
        self.threadLock = threadLock
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1290)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 592)
        self.sfr = sfr
        self.thread_pool = thread_pool

    # ------------------------------------------------------------------------------------------------------------------

    def run(self):
        # capture from web cam
        counter = 0
        while self._run_flag:
            cv_img = self.read_img()
            try:
                frame = getFrame(self.sfr, self.thread_pool, cv_img, counter, self.q, self.threadLock)
                self.change_pixmap_signal.emit(frame)
            except:
                self.cap.release()
                print("exception raised")
            counter += 1
        # shut down capture system
        self.cap.release()

    # ------------------------------------------------------------------------------------------------------------------

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

    # ------------------------------------------------------------------------------------------------------------------

    def get_cap(self) -> cv2.VideoCapture:
        while not self.cap.isOpened():
            self.change_pixmap_signal.emit(cv2.imread("gui/images/no_cam.png"))
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1290)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 592)
        return self.cap

    # ------------------------------------------------------------------------------------------------------------------

    def read_img(self) -> np.ndarray:
        ret1, cv_img = self.get_cap().read()
        if not ret1:
            self.cap.release()
        return cv_img

    @staticmethod
    def rel():
        VideoThread.cap.release()

# ----------------------------------------------------------------------------------------------------------------------
