#!/usr/bin/env python3
"""
Describes the place where the airbnb will be located and description for
the place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class that defines the place where airbnb is located including description
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
