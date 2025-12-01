import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "octopus.sqlite")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev-secret-key-change-in-production"