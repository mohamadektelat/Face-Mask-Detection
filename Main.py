# ----------------------------------------------------------------------------------------------------------------------

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from controller.FaceRecognition import FaceRecognition
from gui.uis.windows.main_window.functions_main_window import *
import sys
import cv2
import numpy as np
from threads.VideoThread import VideoThread
from threads.PicturesThread import PicturesThread
from picBox import *
from queue import Queue
import threading
from datetime import datetime
from PySide6.QtGui import *
# ----------------------------------------------------------------------------------------------------------------------

persons_dict = {}
threadLock = threading.Lock()
thread_pool = ThreadPoolExecutor(max_workers=1)

# ----------------------------------------------------------------------------------------------------------------------

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtWidgets import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# ----------------------------------------------------------------------------------------------------------------------

os.environ["QT_FONT_DPI"] = "96"


# ----------------------------------------------------------------------------------------------------------------------

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
def check_data(name):
    print(name)
    if name[0] == "Unknown":
        return 1
    now = datetime.now()
    if name not in persons_dict:
        persons_dict[name] = now.strftime("%Y%m%d%H%M%S")
        return 2
    if name in persons_dict:
        if (now - datetime.strptime(persons_dict[name], "%Y%m%d%H%M%S")).total_seconds() > 60:
            persons_dict[name] = now.strftime("%Y%m%d%H%M%S")
            return 3
    return 4


# ---------------------------------------------------77------------------------------------------------------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # load encodings
        ###########################################################

        self.sfr = FaceRecognition()
        self.dao = PersonDaoImpl(self.sfr,thread_pool)
        self.sfr.load_encodings(self.dao.getPersonAndEncodings())

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self,self.sfr,thread_pool)


        ###########################################################
        q = Queue()
        # create the video capture thread
        self.thread = VideoThread(q, threadLock, self.sfr, thread_pool)
        self.thread1 = PicturesThread(q, threadLock)

        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread1.page_pixmap_signal.connect(self.add_image_to_page)
        ###########################################################

        # ///////////////////////////////////////////////////////////////
        self.i = 0
        self.j = -1

        # ///////////////////////////////////////////////////////////////

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()
        self.start()

    # ------------------------------------------------------------------------------------------------------------------

    # VIDEO THREAD HANDLING
    # ///////////////////////////////////////////////////////////////
    def start(self):
        self.thread.start()
        self.thread1.start()

    # ------------------------------------------------------------------------------------------------------------------

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    # ------------------------------------------------------------------------------------------------------------------

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.ui.load_pages.stream.setPixmap(qt_img)

    # ------------------------------------------------------------------------------------------------------------------

    @Slot(np.ndarray, str)
    def add_image_to_page(self, cv_img, name):
        """Updates the image_label with a new opencv image"""
        check = check_data(name)
        if check != 4:
            qt_img = self.convert_cv_qt(cv_img)
            object = QLabel()
            box = picBox(self.ui.load_pages.contents)
            # scaling the image
            qt_img = qt_img.scaled(300, 300, Qt.KeepAspectRatio)
            box.setImage(qt_img)
            box.set_data(name, self.dao, cv_img)
            object.setPixmap(qt_img)
            self.ui.load_pages.gridLayout_2.addWidget(box, *self.getPos())
            self.ui.load_pages.right_pic_layout.addWidget(object)

    # ------------------------------------------------------------------------------------------------------------------

    def getPos(self):
        self.j += 1
        if self.j % 3 == 0:
            self.i += 1

        return (self.i, self.j % 3)

    # ------------------------------------------------------------------------------------------------------------------

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_qt_format.scaled(self.ui.load_pages.stream.width(), self.ui.load_pages.stream.height(),
                                        Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    # ------------------------------------------------------------------------------------------------------------------

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)
        # Picture BTN
        if btn.objectName() == "btn_pictures":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        # Add person Button
        if btn.objectName () == "btn_add_person":
            # Select Menu
            self.ui.left_menu.select_only_one (btn.objectName ())
            # Load Page 3
            MainFunctions.set_page (self, self.ui.load_pages.page_3)
            # DEBUG
        #print(f"Button {btn.objectName()}, clicked!")

    # ------------------------------------------------------------------------------------------------------------------

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)
        # DEBUG
        #print(f"Button {btn.objectName()}, released!")

    # ------------------------------------------------------------------------------------------------------------------

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # ------------------------------------------------------------------------------------------------------------------

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# ----------------------------------------------------------------------------------------------------------------------
# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())

# ----------------------------------------------------------------------------------------------------------------------
