#!/usr/bin/python3
import unittest
from models.state import State


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    cls = State()

    def test_state_attributes(self):
        self.assertTrue(hasattr(self.cls, 'id'))
        self.assertTrue(hasattr(self.cls, 'created_at'))
        self.assertTrue(hasattr(self.cls, 'updated_at'))
        self.assertTrue(hasattr(self.cls, 'name'))

    def test_to_dict_method(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()
