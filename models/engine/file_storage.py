#!/usr/bin/env python3
"""
module that serializes instances to JSON file and deserializes JSON file
to instances
"""
import json
import os


class FileStorage:
    """ class that serializes and deserializes instances between objects
    and JSON file
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
        sets the obj with key <obj class name.id>
        """

        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes object to JSON object
        """
        dct = {}
        for key, value in FileStorage.__objects.items():
            dct[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dct, f)

    def reload(self):
        """
        deserializes JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review

        model_class = {'BaseModel': BaseModel, 'User': User, 'State': State,
                       'Amenity': Amenity, 'City': City, 'Place': Place,
                       'Review': Review}
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    self.new(model_class[value['__class__']](**value))
