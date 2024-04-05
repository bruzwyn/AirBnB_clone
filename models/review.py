#!/usr/bin/env python3
"""
model for Review for the airbnb
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class for implementing review of the rooms
    """

    place_id = ""
    user_id = ""
    text = ""
