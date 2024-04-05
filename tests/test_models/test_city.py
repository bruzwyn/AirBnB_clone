#!/usr/bin/env python 3
"""
unittest for city.py
"""
import unittest
from models.city import City
from datetime import datetime


class test_city(unittest.TestCase):
    """
    module for testing city model
    """
    cls = City()

    def test_class_exist(self):
        """ method to test if class exists """

        self.assertEqual(str(type(self.cls)), "<class 'models.city.City'>")

    def test_subclass(self):
        """ test if City is a suclass of BaseModel """

        self.assertTrue(self.cls, City)

    def test_attributes(self):
        """ test the that the type of attributes are correct """

        self.assertIsInstance(self.cls.state_id, str)
        self.assertIsInstance(self.cls.name, str)
        self.assertIsInstance(self.cls.id, str)
        self.assertIsInstance(self.cls.created_at, datetime)
        self.assertIsInstance(self.cls.updated_at, datetime)

    def test_attribute_exists(self):
        """ tests if the attributes exists """

        self.assertTrue(hasattr(self.cls, 'state_id'))
        self.assertTrue(hasattr(self.cls, 'name'))
        self.assertTrue(hasattr(self.cls, 'id'))
        self.assertTrue(hasattr(self.cls, 'created_at'))
        self.assertTrue(hasattr(self.cls, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
