import random

from ..common.base import Base
from .period import Period


class Address(Base):
    """Address

    http://www.hl7.org/fhir/datatypes.html#Address

    An address expressed using postal conventions (as opposed to GPS or other location definition formats). This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery. There are a variety of postal address formats defined around the world.

    Attributes:
      "use"        : "<code>", // home | work | temp | old | billing - purpose of this address
      "type"       : "<code>", // postal | physical | both
      "text"       : "<string>", // Text representation of the address
      "line"       : ["<string>"], // Street name, number, direction & P.O. Box etc.
      "city"       : "<string>", // Name of city, town etc.
      "district"   : "<string>", // District name (aka county)
      "state"      : "<string>", // Sub-unit of country (abbreviations ok)
      "postalCode" : "<string>", // Postal code for area
      "country"    : "<string>", // Country (e.g. can be ISO 3166 2 or 3 letter code)
      "period"     : { Period } // Time period when address was/is in use
    """

    def __init__(self, faker):
        """Init Address Data Type"""
        self.use = random.choice(
            [
                "home",
                "work",
                "temp",
                "temp",
                "old",
                "billing",
            ]
        )
        self.type = random.choice(
            [
                "postal",
                "physical",
                "both",
            ]
        )
        self.text = faker.address()
        self.line = [faker.street_address()]
        self.city = faker.city()
        self.district = faker.city_suffix()
        self.state = faker.city_suffix()
        self.postalCode = faker.postcode()
        self.country = faker.country()
        self.period = Period(faker).serialize()

    def attributes(self):
        """Returns attributes"""
        return {
            "use:": "'<code>', // home | work | temp | old | billing - purpose of this address",
            "type:": "'<code>', // postal | physical | both",
            "text:": "'string>', // Text representation of the address",
            "line:": "['<string>''], // Street name, number, direction & P.O. Box etc.",
            "city:": "'<string>', // Name of city, town etc.",
            "district:": "'<string>', // District name (aka county)",
            "state:": "'<string>', // Sub-unit of country (abbreviations ok)",
            "postalCode:": "'<string>', // Postal code for area",
            "country:": "'<string>', // Country (e.g. can be ISO 3166 2 or 3 letter code)",
            "period:": "{ Period } // Time period when address was/is in use",
        }
