class Base(object):
    DEBUG = False
    SECRET_KEY = "Shhhh is a secret"
    SERVER_NAME="localhost:5000"

class Develop(Base):
    SERVER_NAME="10.100.100.10:5001"