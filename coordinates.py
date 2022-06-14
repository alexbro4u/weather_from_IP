from typing import NamedTuple
import geocoder
from exceptions import CantGetCoordinates 

class Coordinates(NamedTuple):
    latitude: float
    longitude: float 

def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using Host IP"""
    locationData = geocoder.ip('me').latlng
    if locationData is None:
        raise CantGetCoordinates
    latitude,longitude = locationData[0],locationData[1]
    return Coordinates(latitude=latitude,longitude=longitude)

if __name__ == "__main__":
    print(get_gps_coordinates())