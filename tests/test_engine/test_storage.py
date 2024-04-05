#!/usr/bin/env python3
"""
tests FileStorage module
"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
import json
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):
    """ test suit for file storage tests """

    cls = BaseModel()

    def test_instance(self):
        self.assertIsInstance(storage, FileStorage)

    def test_has_attributes(self):
        """ check if attributes exists """

        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_store_base_model(self):
        """ test for save, to_dict, and reload method """

        self.cls.full_name = "BaseModel Instance"
        self.cls.save()
        dct = self.cls.to_dict()
        objs = storage.all()
        key = dct['__class__'] + '.' + dct['id']
        self.assertEqual(key in objs, False)

    def test_save(self):
        """ verify JSON file exists """

        self.cls.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """ tests reload method """

        self.cls.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        objs = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(objs, FileStorage._FileStorage__objects)

    def test_new(self):
        """tests new method """

        data = self.cls.to_dict()
        key = data['__class__'] + '.' + data['id']
        storage.save()
        with open("file.json", "r") as f:
            dat2 = json.load(f)
        new = dat2[key]
        for k in new:
            self.assertEqual(data[k], new[k])

    def test_save2(self):
        msg = 'FileStorage' + '.'
        msg = msg + "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unttest.main()
