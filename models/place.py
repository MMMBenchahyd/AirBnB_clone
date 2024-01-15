#!/usr/bin/python3
"""
Module for the Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
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