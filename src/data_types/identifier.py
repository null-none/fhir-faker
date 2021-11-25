import random
from datetime import date

from period import Period
from common.base import Base


class Identifier(Base):
    """Identifier

    https://www.hl7.org/fhir/datatypes.html#Identifier

    A numeric or alphanumeric string that is associated with a single object or entity within a given system. Typically, identifiers are used to connect content in resources to external content available in other frameworks or protocols. Identifiers are associated with objects and may be changed or retired due to human or system process and errors.

    Attributes:
      "use" : "<code>", // usual | official | temp | secondary | old (If known)
      "type" : { CodeableConcept }, // Description of identifier
      "system" : "<uri>", // The namespace for the identifier value
      "value" : "<string>", // The value that is unique
      "period" : { Period }, // Time period when id is/was valid for use
      "assigner" : { Reference(Organization) } // Organization that issued id (may be just text)
    """

    def __init__(self, faker):
        """Init Identifier Data Type"""
        self.use = random.choice(["usual", "official", "temp", "secondary", "old"])
        self.period = Period(faker).serialize()

    def attributes(self):
        """Returns attributes"""
        return {
            "use": "'<code>', // usual | official | temp | secondary | old (If known)",
            "type": "{ CodeableConcept }, // Description of identifier",
            "system": "'<uri>', // The namespace for the identifier value",
            "value": "'<string>', // The value that is unique",
            "period": "{ Period }, // Time period when id is/was valid for use",
            "assigner": "{ Reference(Organization) } // Organization that issued id (may be just text)",
        }
