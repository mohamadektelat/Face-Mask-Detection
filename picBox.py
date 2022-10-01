# ----------------------------------------------------------------------------------------------------------------------


from PySide6.QtWidgets import *

from database.personDaoImpl import *
from messages.ChatPot import send_email

# ----------------------------------------------------------------------------------------------------------------------

persons_dict = {}


# ----------------------------------------------------------------------------------------------------------------------

class picBox(QFrame):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self, parent,  *args, **kwargs):
        super().__init__(parent,*args, **kwargs)

        self.setStyleSheet(frame_style)
        self.verticalLayout = QVBoxLayout(self)

        self.image = QLabel(self)
        #self.image.setStyleSheet(style)
        self.name = QLabel(self)
        self.email = QLabel(self)
        self.phone_number = QLabel(self)

        self.verticalLayout.addWidget(self.image)
        self.verticalLayout.addWidget(self.name)
        self.verticalLayout.addWidget(self.email)
        self.verticalLayout.addWidget(self.phone_number)



    # ------------------------------------------------------------------------------------------------------------------

    def setImage(self, img):
        self.image.setPixmap(img)

    # ------------------------------------------------------------------------------------------------------------------

    def set_data(self, name, dao: PersonDaoImpl, cv_img):
        fullname = name[0] + ' ' + name[1]
        if fullname.rstrip() != "Unknown":
            person = dao.get_person_by_name(name[0], name[1])
            self.name.setText(fullname)
            self.email.setText(person.email)
            self.phone_number.setText(person.phone_number)
            send_email(fullname, person.email, cv_img)
            return
        self.name.setText(fullname)
        self.email.setText("")
        self.phone_number.setText("")

# ----------------------------------------------------------------------------------------------------------------------

style = '''
QLabel{
    border: 2px solid green;
    border-radius: 4px;
    padding: 2px;
    }
'''

frame_style = '''
QFrame{
background-color:rgb(33, 37, 45);
}
'''