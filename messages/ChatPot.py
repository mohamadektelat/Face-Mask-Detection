# ----------------------------------------------------------------------------------------------------------------------

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cv2
import PIL.Image as Image
import io

# ----------------------------------------------------------------------------------------------------------------------

user = "maskdetection.program@gmail.com"
password = "iqtfhpyqurelbcmw"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, password)


# ----------------------------------------------------------------------------------------------------------------------

def email_alert(subject, body, to, cv_img):
    msg = MIMEMultipart()
    img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(img)
    byte = io.BytesIO()
    pil_im.save(byte, 'jpeg')
    im_bytes = byte.getvalue()
    image = MIMEImage(im_bytes)
    text = MIMEText(body)
    msg.attach(text)
    msg['subject'] = subject
    msg['From'] = "maskdetection.program@gmail.com"
    msg['to'] = to
    msg.attach(image)
    user = "maskdetection.program@gmail.com"
    msg['from'] = user
    server.send_message(msg)


# ----------------------------------------------------------------------------------------------------------------------

def quite():
    server.quit()


# ----------------------------------------------------------------------------------------------------------------------

def send_email(name, email, cv_img):
    email_alert("No mask detection", "hey {}, please put your mask!!!!".format(name), email, cv_img)

# ----------------------------------------------------------------------------------------------------------------------