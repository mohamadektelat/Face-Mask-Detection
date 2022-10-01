# ----------------------------------------------------------------------------------------------------------------------

import sqlite3
import os.path

# ----------------------------------------------------------------------------------------------------------------------

class Connection_pool():
    __instance = None

    # ------------------------------------------------------------------------------------------------------------------

    class Connection_pool(object):
        def __new__(cls):
            if not hasattr (cls, 'instance'):
                cls.instance = super(Connection_pool, cls).__new__ (cls)
            return cls.instance

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        pass

    # ------------------------------------------------------------------------------------------------------------------

    def get_connection(self):
        BASE_DIR = os.path.dirname (os.path.abspath ("face_mask.db"))
        db_path = os.path.join (BASE_DIR, "face_mask.db")
        return sqlite3.connect(db_path)

    # ------------------------------------------------------------------------------------------------------------------

    def close_connection(self, con):
        try:
            con.close()
            print ("sqlite connection is closed")
        except Error as e:
            print ("Error while connecting to sqlite using Connection pool ", e)

# ----------------------------------------------------------------------------------------------------------------------
