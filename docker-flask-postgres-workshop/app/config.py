
import os

class Config:
    # Change stimsina-db to yourusername-db
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@stimsina-db:5432/workshop_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
