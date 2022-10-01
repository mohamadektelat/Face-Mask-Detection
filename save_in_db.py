import json

import numpy
import pandas

"""
from personDaoImpl import *


dao = PersonDaoImpl()

dao.get_person_by_name('abedallah','joulany')
"""
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath("face_mask.db"))
db_path = os.path.join(BASE_DIR, "face_mask.db")
conn = sqlite3.connect(db_path)
print("Opened database successfully")

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

arr = numpy.array([-0.10213576,  0.05088161, -0.03425048, -0.09622347, -0.12966095,
        0.04867411, -0.00511892, -0.03418527,  0.2254715 , -0.07892745,
        0.21497472, -0.0245543 , -0.2127848 , -0.08542262, -0.00298059,
        0.13224372, -0.21870363, -0.09271716, -0.03727289, -0.1250658 ,
        0.09436664,  0.03037129, -0.02634972,  0.02594662, -0.1627259 ,
       -0.29416466, -0.12254384, -0.15237436,  0.14907973, -0.09940194,
        0.02000656,  0.04662619, -0.1266906 , -0.11484023,  0.04613583,
        0.1228286 , -0.03202137, -0.0715076 ,  0.18478717, -0.01387333,
       -0.11409076,  0.07516225,  0.08549548,  0.31538364,  0.1297821 ,
        0.04055009,  0.0346106 , -0.04874525,  0.17533901, -0.22634712,
        0.14879328,  0.09331974,  0.17943285,  0.02707857,  0.22914577,
       -0.20668915,  0.03964197,  0.17524502, -0.20210043,  0.07155308,
        0.04467429,  0.02973968,  0.00257265, -0.00049853,  0.18866715,
        0.08767469, -0.06483966, -0.13107982,  0.21610288, -0.04506358,
       -0.02243116,  0.05963502, -0.14988004, -0.11296406, -0.30011353,
        0.07316103,  0.38660526,  0.07268623, -0.14636359,  0.08436179,
        0.01005938, -0.00661338,  0.09306039,  0.03271955, -0.11528577,
       -0.0524189 , -0.11697718,  0.07356471,  0.10350288, -0.03610475,
        0.00390615,  0.17884226,  0.04291092, -0.02914601,  0.06112404,
        0.05315027, -0.14561613, -0.01887275, -0.13125736, -0.0362937 ,
        0.16490118, -0.09027836, -0.00981111,  0.1363602 , -0.23134531,
        0.0788044 , -0.00604869, -0.05569676, -0.07010217, -0.0408107 ,
       -0.10358225,  0.08519378,  0.16833456, -0.30366772,  0.17561394,
        0.14421709, -0.05016343,  0.13464174,  0.0646335 , -0.0262765 ,
        0.02722404, -0.06028951, -0.19448066, -0.07304715,  0.0204969 ,
       -0.03045784, -0.02818791,  0.06679841])

conn.execute(create_person_table)
conn.execute(create_encoding_table)

str_two_d = []
str_list = [str(x) for x in arr]
str_two_d.append(str_list)
str_two_d.append(str_list)

#print(json.dumps(str_two_d))
"""conn.execute ('INSERT INTO person (id_number, first_name, last_name, email, phone_number)'
              ' VALUES(?,?,?,?,?);',("123","abed","jou","mabed@edu.hac.ac.il","052848614"))"""

"""for i in str_two_d:
    conn.execute('INSERT INTO encoding (id_number, encode)'
             ' VALUES(?,?);',("123",json.dumps(i)))

conn.commit()"""


#cursor = conn.execute('SELECT first_name, last_name, encode FROM person natural join encoding')
cursor = conn.execute('SELECT * FROM person where first_name = "abedallah" and last_name = "joulany";')
print(cursor.fetchall())
for row in cursor:
    print (row)
    #encodes = json.loads(row[2])
    #l = [numpy.float64 (x) for x in encodes]

"""    enodes = json.loads(row[2])
    for col in enodes:
        l = [numpy.float64 (x) for x in col]
        print(l)"""


"""sql = 'drop table person'
sql2 = 'drop table encoding'
cur = conn.cursor()
cur.execute(sql2)
cur.execute(sql)
conn.commit()"""


conn.close()
