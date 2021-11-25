import random
from datetime import date

from common.base import Base
from period import Period


class ContactPoint(Base):
    """ContactPoint

    https://www.hl7.org/fhir/datatypes.html#ContactPoint

    Details for all kinds of technology-mediated contact points for a person or organization, including telephone, email, etc.

    Attributes:
      "system" : "<code>", // C? phone | fax | email | pager | url | sms | other
      "value"  : "<string>", // The actual contact point details
      "use"    : "<code>", // home | work | temp | old | mobile - purpose of this contact point
      "rank"   : "<positiveInt>", // Specify preferred order of use (1 = highest)
      "period" : { Period } // Time period when the contact point was/is in use
    """

    def __init__(self, faker):
        """Init ContactPoint Data Type"""
        self.use = random.choice(["phone", "sms"])
        self.value = faker.phone_number()
        self.use = random.choice(["home", "work", "temp", "old", "mobile"])
        self.rank = 1
        self.period = Period(faker).serialize()

    def attributes(self):
        """Returns attributes"""
        return {
            "system": "'<code>', // C? phone | fax | fax | fax | url | sms | other",
            "value": "'<string>', // The actual contact point details",
            "use": "'<code>', // home | work | temp | old | mobile - purpose of this contact point",
            "rank": "'<positiveInt>', // Specify preferred order of use (1 = highest)",
            "period": "{ Period } // Time period when the contact point was/is in use",
        }
