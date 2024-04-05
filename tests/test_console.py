#!/usr/bin/env python3
"""
this module test consol module using unittest.TesCase and Mock module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()
        self.hbnb.prompt = ""

    def tearDown(self):
        self.hbnb = None

    def assert_output(self, command, expected_output):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb.onecmd(command)
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, expected_output)

    def test_do_quit(self):
        self.assertTrue(self.hbnb.do_quit(None))

    def test_do_EOF(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb.do_EOF(None)
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, '')

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb.emptyline()
            actual_output = mock_stdout.getvalue().strip()
            self.assertEqual(actual_output, '')

    def test_do_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb.do_create("BaseModel")
            actual_output = mock_stdout.getvalue().strip()
            self.assertTrue(actual_output != '')

    def test_do_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb.do_create("BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            self.hbnb.onecmd(f"show BaseModel {instance_id}")
            actual_output = mock_stdout.getvalue().strip()
            self.assertTrue(actual_output != '')

    def test_do_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb.do_create("BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            self.hbnb.onecmd(f"destroy BaseModel {instance_id}")
            self.hbnb.onecmd(f"show BaseModel {instance_id}")
            actual_output = mock_stdout.getvalue().strip()
            self.assertTrue("** no instance found **" in actual_output)

    def test_do_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb.do_create("BaseModel")
            self.hbnb.do_create("BaseModel")
            self.hbnb.do_create("User")
            self.hbnb.onecmd("all BaseModel")
            actual_output = mock_stdout.getvalue().strip()
            self.assertTrue(actual_output != '')

    def test_do_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb.do_create("BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            self.hbnb.onecmd(f"update BaseModel {instance_id} name John")
            self.hbnb.onecmd(f"show BaseModel {instance_id}")
            actual_output = mock_stdout.getvalue().strip()
            self.assertTrue("John" in actual_output)


if __name__ == '__main__':
    unittest.main()
