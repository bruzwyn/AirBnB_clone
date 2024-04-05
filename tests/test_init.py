#!/usr/bin/python3
import unittest
from models import storage


class TestInit(unittest.TestCase):
    """Test cases for the __init__.py file"""

    def test_storage_instance(self):
        self.assertIsNotNone(storage)
        self.assertTrue(hasattr(storage, 'reload'))

    def test_reload_method(self):
        self.assertTrue(hasattr(storage, 'reload'))

        try:
            storage.reload()
        except Exception as e:
            self.fail(f"reload method raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
