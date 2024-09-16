# config/config.py

import os

class Config:
    
    # configuracion eseba
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/finance_db'
    
    # configuracion navio
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:sasa@localhost/finance_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
