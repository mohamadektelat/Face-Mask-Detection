# ----------------------------------------------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor
from database.ConnectionPool import *
from database.Person import Person
import json
import numpy
import cv2
import face_recognition
from controller.FaceRecognition import FaceRecognition
# ----------------------------------------------------------------------------------------------------------------------


get_person_query_by_name = 'SELECT * FROM person where first_name = "{}" and last_name = "{}";'
get_person_query_by_id = 'SELECT * FROM person where id_number = "{}";'
get_person_encoding = 'SELECT * FROM person natural join encoding'
get_person_query_by_name_encoding = 'SELECT first_name, last_name, encode FROM person natural join encoding'

insert_person_query = 'INSERT INTO person (id_number, first_name, last_name, email, phone_number)\
                       VALUES("{}","{}","{}","{}","{}");'
insert_encoding_query = 'INSERT INTO encoding (id_number, encode)\
                       VALUES("{}","{}");'

create_person_table = '''CREATE TABLE IF NOT EXISTS person
  (id_number INT UNSIGNED PRIMARY KEY NOT NULL UNIQUE,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL ,
  email TEXT NOT NULL UNIQUE,
  phone_number TEXT NOT NULL UNIQUE
  );
  '''
create_encoding_table = '''CREATE TABLE IF NOT EXISTS encoding
  (
  encode TEXT NOT NULL,
  id_number INT UNSIGNED NOT NULL,
  FOREIGN KEY (id_number) REFERENCES person (id_number)
  );
  '''

drop_person_table = 'drop table person'
drop_encoding_table = 'drop table encoding'
# ----------------------------------------------------------------------------------------------------------------------


def insert_encoding(sfr: FaceRecognition, pool, name, id, images: [str]):

    connection = pool.get_connection()
    for img in images:
        image = cv2.imread (img)
        rgb_img = cv2.cvtColor (image, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(rgb_img, model="hog", num_jitters=50)[0]
        str_list = [str (x) for x in encoding]
        connection.execute ('INSERT INTO encoding (id_number, encode)\
         VALUES(?,?);', (id, json.dumps (str_list)))
        sfr.append_known_face_names(name)
        sfr.append_known_face_encoding(encoding)
    connection.commit ()
    connection.close ()


class PersonDaoImpl(object):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self, sfr: FaceRecognition, thread_pool):
        self.pool = Connection_pool()
        self.connection = self.pool.get_connection()
        self.connection.execute(create_person_table)
        self.connection.execute(create_encoding_table)
        self.sfr = sfr
        self.thread_pool = thread_pool

    # ------------------------------------------------------------------------------------------------------------------

    def get_person_by_name(self, first, last):
        cursor = self.connection.execute(get_person_query_by_name.format(str.lower(first), str.lower(last)))
        result = cursor.fetchall()
        if not result:
            return Person(['Unknown', 'Person', ' ', ' ', ' '])
        return Person(result[0])

    # ------------------------------------------------------------------------------------------------------------------

    def get_person_by_id(self, id_num):
        cursor = self.connection.execute(get_person_query_by_id.format(id_num))
        result = cursor.fetchall()
        if not result:
            return Person(['Unknown','Person',' ',' ',' '])
        return Person(result[0])

    # ------------------------------------------------------------------------------------------------------------------

    def add_person(self, person,images:[str]):
        self.connection.execute (insert_person_query.format
                            (person.id_number, person.first_name, person.last_name, person.email,
                             person.phone_number))
        self.connection.commit ()
        #name = person.first_name + ' ' + person.last_name

        self.thread_pool.submit(insert_encoding,self.sfr, self.pool, (person.first_name, person.last_name), person.id_number,images)


    def getPersonAndEncodings(self):
        name_encoding = []
        cursor = self.connection.execute (get_person_query_by_name_encoding)
        for row in cursor:
            name = row[0] + ' ' + row[1]
            enodes = json.loads(row[2])
            l = [numpy.float64 (x) for x in enodes]
            name_encoding.append (((row[0],row[1]), l))
        return name_encoding

    def delete_tables(self):
        cursor = self.connection.cursor()
        cursor.execute(drop_encoding_table)
        cursor.execute(drop_person_table)
        self.connection.commit()
        self.create_tables()
        self.sfr.known_face_encodings.clear()
        self.sfr.known_face_names.clear()

    def create_tables(self):
        self.connection.execute(create_person_table)
        self.connection.execute(create_encoding_table)
        self.connection.commit()

# ----------------------------------------------------------------------------------------------------------------------
