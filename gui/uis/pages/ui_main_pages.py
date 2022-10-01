# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesYGodkX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtWidgets import QLabel as QtLabel
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Ui_MainPages (object):
    def setupUi(self, MainPages):
        if MainPages.objectName ():
            MainPages.setObjectName (u"MainPages")
        MainPages.resize (1125, 628)
        self.main_pages_layout = QVBoxLayout (MainPages)
        self.main_pages_layout.setSpacing (0)
        self.main_pages_layout.setObjectName (u"main_pages_layout")
        self.main_pages_layout.setContentsMargins (0, 0, 0, 0)
        self.pages = QStackedWidget (MainPages)
        self.pages.setObjectName (u"pages")
        self.page_1 = QWidget ()
        self.page_1.setObjectName (u"page_1")
        self.page_1.setStyleSheet (u"font-size: 14pt")
        self.horizontalLayout_2 = QHBoxLayout (self.page_1)
        self.horizontalLayout_2.setSpacing (5)
        self.horizontalLayout_2.setObjectName (u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins (5, 5, 5, 5)
        self.frame_1 = QFrame (self.page_1)
        self.frame_1.setObjectName (u"frame_1")
        self.frame_1.setMinimumSize (QSize (860, 600))
        self.frame_1.setMaximumSize (QSize (16777215, 16777215))
        self.frame_1.setFrameShape (QFrame.StyledPanel)
        self.frame_1.setFrameShadow (QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout (self.frame_1)
        self.horizontalLayout_3.setObjectName (u"horizontalLayout_3")
        self.stream = QLabel (self.frame_1)
        self.stream.setObjectName (u"stream")
        self.stream.setMinimumSize (QSize (1300, 600))
        self.stream.setMaximumSize (QSize (16777215, 16777215))

        self.horizontalLayout_3.addWidget (self.stream)

        self.horizontalLayout_2.addWidget (self.frame_1)

        self.scrollArea = QScrollArea (self.page_1)
        self.scrollArea.setObjectName (u"scrollArea")
        self.scrollArea.setMinimumSize (QSize (240, 0))
        self.scrollArea.setStyleSheet (u"background: transparent;")
        self.scrollArea.setWidgetResizable (True)
        self.scrollAreaWidgetContents_2 = QWidget ()
        self.scrollAreaWidgetContents_2.setObjectName (u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry (QRect (0, 0, 238, 616))
        self.scrollAreaWidgetContents_2.setMinimumSize (QSize (0, 0))
        self.scrollAreaWidgetContents_2.setStyleSheet (u"background: transparent;\n"
                                                       "")
        self.verticalLayout = QVBoxLayout (self.scrollAreaWidgetContents_2)
        self.verticalLayout.setSpacing (0)
        self.verticalLayout.setObjectName (u"verticalLayout")
        self.verticalLayout.setContentsMargins (0, 0, 0, 0)
        self.frame_2 = QFrame (self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName (u"frame_2")
        self.frame_2.setFrameShape (QFrame.StyledPanel)
        self.frame_2.setFrameShadow (QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout (self.frame_2)
        self.verticalLayout_3.setSpacing (0)
        self.verticalLayout_3.setObjectName (u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins (0, 0, 0, 0)
        self.right_pic_layout = QVBoxLayout ()
        self.right_pic_layout.setObjectName (u"right_pic_layout")

        self.verticalLayout_3.addLayout (self.right_pic_layout)

        self.verticalLayout.addWidget (self.frame_2)

        self.scrollArea.setWidget (self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget (self.scrollArea)

        self.pages.addWidget (self.page_1)
        self.page_2 = QWidget ()
        self.page_2.setObjectName (u"page_2")
        self.page_2_layout = QVBoxLayout (self.page_2)
        self.page_2_layout.setSpacing (5)
        self.page_2_layout.setObjectName (u"page_2_layout")
        self.page_2_layout.setContentsMargins (5, 5, 5, 5)
        self.scroll_area = QScrollArea (self.page_2)
        self.scroll_area.setObjectName (u"scroll_area")

        self.scroll_area.setStyleSheet (u'''QScrollArea{background: transparent;}
                                        ''')
        self.scroll_area.setFrameShape (QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy (Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy (Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable (True)
        self.contents = QWidget ()
        self.contents.setObjectName (u"contents")
        self.contents.setGeometry (QRect (0, 0, 1100, 618))
        self.contents.setStyleSheet (u"background: transparent;")
        self.verticalLayout2 = QVBoxLayout (self.contents)
        self.verticalLayout2.setObjectName (u"verticalLayout2")
        self.gridLayout_2 = QGridLayout ()
        self.gridLayout_2.setSpacing (25)
        self.gridLayout_2.setObjectName (u"gridLayout_2")
        self.gridLayout_2.setContentsMargins (6, -1, 6, -1)

        self.verticalLayout2.addLayout (self.gridLayout_2)
        self.scroll_area.setWidget (self.contents)
        self.page_2_layout.addWidget (self.scroll_area)
        self.pages.addWidget (self.page_2)

        # page 3
        #####################################################
        self.page_3 = QWidget ()
        self.page_3.setObjectName (u"page_3")
        self.page_3_layout = QVBoxLayout (self.page_3)
        self.page_3_layout.setSpacing (5)
        self.page_3_layout.setObjectName (u"page_3_layout")
        self.page_3_layout.setContentsMargins (5, 5, 5, 5)
        self.scroll_area3 = QScrollArea (self.page_3)
        self.scroll_area3.setObjectName (u"scroll_area")
        self.scroll_area3.setStyleSheet (u"background: transparent;")
        self.scroll_area3.setFrameShape (QFrame.NoFrame)
        self.scroll_area3.setVerticalScrollBarPolicy (Qt.ScrollBarAlwaysOff)
        self.scroll_area3.setHorizontalScrollBarPolicy (Qt.ScrollBarAlwaysOff)
        self.scroll_area3.setWidgetResizable (True)
        self.contents = QWidget ()
        self.contents.setObjectName (u"contents")
        self.contents.setGeometry (QRect (0, 0, 840, 580))
        self.contents.setStyleSheet (u"background: transparent;")
        self.verticalLayout = QVBoxLayout (self.contents)
        self.verticalLayout.setSpacing (15)
        self.verticalLayout.setObjectName (u"verticalLayout")
        self.verticalLayout.setContentsMargins (5, 5, 5, 5)
        # setting the alignment top
        self.verticalLayout.setAlignment (Qt.AlignTop)
        self.title_label = QLabel (self.contents)
        self.title_label.setObjectName (u"title_label")
        self.title_label.setMaximumSize (QSize (16777215, 40))
        font = QFont ()
        font.setPointSize (16)
        self.title_label.setFont (font)
        self.title_label.setStyleSheet (u"font-size: 16pt")
        self.title_label.setAlignment (Qt.AlignCenter)

        self.verticalLayout.addWidget (self.title_label)
        # description label
        self.description_label = QLabel (self.contents)
        self.description_label.setObjectName (u"description_label")
        self.description_label.setAlignment (Qt.AlignHCenter | Qt.AlignTop)
        self.description_label.setWordWrap (True)
        self.verticalLayout.addWidget (self.description_label)

        ########### rows ##############
        # row 1
        self.row_1_layout = QHBoxLayout ()
        self.row_1_layout.setObjectName (u"row_1_layout")
        self.verticalLayout.addLayout (self.row_1_layout)

        # row 2
        self.row_2_layout = QHBoxLayout ()
        self.row_2_layout.setObjectName (u"row_2_layout")
        self.verticalLayout.addLayout (self.row_2_layout)
        ## row 3
        self.row_3_layout = QHBoxLayout ()
        self.row_3_layout.setObjectName (u"row_3_layout")
        self.verticalLayout.addLayout (self.row_3_layout)
        # row 4
        self.row_4_layout = QHBoxLayout ()
        self.row_4_layout.setObjectName (u"row_4_layout")
        self.row_4_layout.setAlignment (Qt.AlignLeft)
        self.verticalLayout.addLayout (self.row_4_layout)
        # row 5
        self.row_5_layout = QHBoxLayout ()
        self.row_5_layout.setObjectName (u"row_0_layout")
        self.row_5_layout.setAlignment (Qt.AlignLeft)
        self.verticalLayout.addLayout (self.row_5_layout)

        self.scroll_area3.setWidget (self.contents)
        self.page_3_layout.addWidget (self.scroll_area3)
        self.pages.addWidget (self.page_3)
        #########################################################

        self.main_pages_layout.addWidget (self.pages)
        self.retranslateUi (MainPages)

        self.pages.setCurrentIndex (0)

        QMetaObject.connectSlotsByName (MainPages)

    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle (QCoreApplication.translate ("MainPages", u"Form", None))
        self.stream.setText ("")
        self.title_label.setText (QCoreApplication.translate ("MainPages", u"DataBase Page", None))
        self.description_label.setText (QCoreApplication.translate ("MainPages",
                                                                    u"Here we can add unkown persons to the datebase.\n",
                                                                    None))

    # retranslateUi
