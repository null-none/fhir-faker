import random
from datetime import date

from common.base import Base


class Period(Base):
    """Period

    https://www.hl7.org/fhir/datatypes.html#Period

    A time period defined by a start and end date/time.
    A period specifies a range of times. The context of use will specify whether the entire range applies (e.g. "the patient was an inpatient of the hospital for this time range") or one value from the period applies (e.g. "give to the patient between 2 and 4 pm on 24-Jun 2013").

    Attributes:
        "start" : "<dateTime>", // C? Starting time with inclusive boundary
        "end"   : "<dateTime>" // C? End time with inclusive boundary, if not ongoing
    """

    def __init__(self, faker):
        """Init Period Data Type"""
        self.start = faker.date_of_birth(minimum_age=5, maximum_age=60)
        self.end = date.today()

    def attributes(self):
        """Returns attributes"""
        return {
            "start:": "'<dateTime>', // C? Starting time with inclusive boundary",
            "end": "'<dateTime>', //C? End time with inclusive boundary, if not ongoing",
        }
