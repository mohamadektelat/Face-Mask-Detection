# ----------------------------------------------------------------------------------------------------------------------

import time
from PySide6.QtCore import *

import numpy as np


# ----------------------------------------------------------------------------------------------------------------------

class PicturesThread(QThread):
    page_pixmap_signal = Signal(np.ndarray, tuple)

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, q, threadLock):
        super().__init__()
        self.q = q
        self._run_flag = True
        self.threadLock = threadLock

    # ------------------------------------------------------------------------------------------------------------------

    def run(self):
        while self._run_flag:
            if not self.q.empty():
                try:
                    self.threadLock.acquire()
                    img_name = self.q.get()
                    self.page_pixmap_signal.emit(img_name[0], img_name[1])
                    self.threadLock.release()
                except:
                    print("thread error")
            time.sleep(0.2)

    # ------------------------------------------------------------------------------------------------------------------

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()
# ----------------------------------------------------------------------------------------------------------------------
