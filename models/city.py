#!/usr/bin/env python3
"""
Defines the city for the airbnb
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class to implement city for the airbnb house
    """

    state_id = ""
    name = ""
