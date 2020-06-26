import os
def config(object):
    SECRET_KEY = os.urandom(32)
    MONGODB_SETTINGS={'db':'HotelManagement'}