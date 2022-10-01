

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import threading

from database.personDaoImpl import PersonDaoImpl
from database.Person import Person
from picBox import picBox
from . functions_main_window import *
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes
# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *
# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *
from concurrent.futures import ThreadPoolExecutor
# PY WINDOW
import cv2
# ///////////////////////////////////////////////////////////////
pool = ThreadPoolExecutor(max_workers=1)
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.files = [str]

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },

        {
            "btn_icon" : "no_icon.svg",
            "btn_id" : "btn_pictures",
            "btn_text" : "show pictures",
            "btn_tooltip" : "show pictures",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon": "icon_add_user.svg",
            "btn_id": "btn_add_person",
            "btn_text": "Add Person",
            "btn_tooltip": "Add person",
            "show_top": True,
            "is_active": False
        },
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.load_pages.row_3_layout.sender() != None:
            return self.ui.load_pages.row_3_layout.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self, sfr, thread_pool):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # page 3 - database
        # ///////////////////////////////////////////////////////////////
        # PY LINE EDIT
        self.line_fisrt_name = PyLineEdit (
            text="",
            place_holder_text="First name",
            radius=8,
            border_size=3,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_fisrt_name.setMinimumHeight (40)

        self.line_last_name = PyLineEdit (
            text="",
            place_holder_text="Last name",
            radius=8,
            border_size=3,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_last_name.setMinimumHeight (40)

        self.line_id = PyLineEdit (
            text="",
            place_holder_text="id",
            radius=8,
            border_size=3,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_id.setMinimumHeight (40)

        self.line_email = PyLineEdit (
            text="",
            place_holder_text="Email",
            radius=8,
            border_size=3,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_email.setMinimumHeight (40)

        self.line_phone_number = PyLineEdit (
            text="",
            place_holder_text="Phone number",
            radius=8,
            border_size=3,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_phone_number.setMinimumHeight (40)
        self.line_phone_number.setMaximumWidth (637)

        def dialog():

            def convert_cv_qt(cv_img):
                """Convert from an opencv image to QPixmap"""
                rgb_image = cv2.cvtColor (cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QImage (rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_qt_format.scaled (self.ui.load_pages.stream.width (),
                                                 self.ui.load_pages.stream.height (),
                                                 Qt.KeepAspectRatio)
                return QPixmap.fromImage (p)

            self.files, check = QFileDialog.getOpenFileNames(None, "Open files",
                                                       "images", "Image files (*.jpg *.jpeg *.png)")
            if len(self.files) > 0:
                for i in reversed(range (self.grid_pictures.count ())):
                    self.grid_pictures.itemAt (i).widget ().setParent (None)
                x , y = 0, 0
                for i in self.files:
                    img = cv2.imread (i)
                    qt_img = self.convert_cv_qt(img)
                    object = QLabel ()
                    # scaling the image
                    img = qt_img.scaled (300, 300, Qt.KeepAspectRatio)
                    object.setPixmap (img)
                    self.grid_pictures.addWidget(object,*(x,y%5))
                    y += 1
                    if y % 5 == 0:
                        x += 1

        # PUSH BUTTON 1
        self.button_choose_images = PyPushButton (
            text="Choose images",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.button_choose_images.setMinimumHeight (40)
        self.button_choose_images.clicked.connect(dialog)

        # Add Person BUTTON
        self.button_add_person = PyIconButton (
            icon_path=Functions.set_svg_icon ("icon_add_user.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="add person",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
        )

        # grid for chosen pictures
        self.grid_pictures = QGridLayout ()

        def clear_fields():
            self.line_fisrt_name.clear()
            self.line_last_name.clear()
            self.line_id.clear()
            self.line_email.clear()
            self.line_phone_number.clear()
            for i in reversed (range (self.grid_pictures.count ())):
                self.grid_pictures.itemAt (i).widget ().setParent (None)

        def add_to_db():
            dao = PersonDaoImpl(sfr, thread_pool)
            dao.add_person(Person([self.line_id.text(),self.line_fisrt_name.text(),
                                  self.line_last_name.text(), self.line_email.text(),self.line_phone_number.text()]),
                                  [i for i in self.files])
            clear_fields()

        self.button_add_person.clicked.connect(add_to_db)

        # clear fields button
        self.button_clear_fields = PyIconButton (
            icon_path=Functions.set_svg_icon ("icon_close.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="clear all fields",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
        )
        self.button_clear_fields.clicked.connect(clear_fields)

        # button to reset database
        self.button_reset_database = PyPushButton (
            text="Reset Database",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.button_reset_database.setMinimumHeight (40)
        self.button_reset_database.setMinimumWidth(400)
        def reset_database():
            dao = PersonDaoImpl (sfr, thread_pool)
            dao.delete_tables()
        self.button_reset_database.clicked.connect (reset_database)


        # ADD WIDGETS
        self.ui.load_pages.row_1_layout.addWidget(self.line_fisrt_name)
        self.ui.load_pages.row_1_layout.addWidget(self.line_last_name)
        self.ui.load_pages.row_2_layout.addWidget(self.line_id)
        self.ui.load_pages.row_2_layout.addWidget(self.line_email)
        self.ui.load_pages.row_3_layout.addWidget(self.line_phone_number)
        self.ui.load_pages.row_3_layout.addWidget(self.button_choose_images)
        self.ui.load_pages.row_3_layout.addWidget(self.button_add_person)
        self.ui.load_pages.row_3_layout.addWidget(self.button_clear_fields)
        self.ui.load_pages.row_4_layout.addWidget(self.button_reset_database)
        self.ui.load_pages.row_5_layout.addLayout(self.grid_pictures)

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)