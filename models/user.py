#!/usr/bin/env python3
"""
This is module is used to define a new user of the program
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that defines a new user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
