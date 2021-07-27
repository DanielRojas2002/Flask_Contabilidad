import os

from flask_sqlalchemy import SQLAlchemy
class Config(object):
    SECRET_KEY='a7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    DEBUG=True
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME='danielerojas2002@gmail.com'
    MAIL_PASSWORD='1234'

class DeveloperConfig(Config):
    SQLAlCHEMY_DATABASE_URI='mysql+pymysql://daniel:12+@localhost/our_users'
    SQLAlCHEMY_TRACK_MODIFICATION=False 