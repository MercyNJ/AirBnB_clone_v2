#previous one
#!/usr/bin/python3
"""__init__ magic method for models directory
and creates a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    BaseModel.storage_type = "db"
else:
    storage = FileStorage()
    BaseModel.storage_type = "file_storage"
storage.reload()
