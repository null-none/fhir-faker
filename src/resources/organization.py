import random
import uuid

from common.base import Base
from data_types.human_name import HumanName
from data_types.address import Address


class Organization(Base):
    """Organization

    https://www.hl7.org/fhir/organization.html

    Demographics and other administrative information about an individual or animal receiving care or other health-related services.

    Attributes:
      "resourceType"         : "Organization",
      "identifier"           : [{ Identifier }], // C? Identifies this organization  across multiple systems
      "active"               : <boolean>, // Whether the organization's record is still in active use
      "name"                 : "<string>", // C? Name used for the organization
    """

    def __init__(self, faker):
        """Init Organization Resource"""
        self.resourceType = "Organization"
        self.identifier = uuid.uuid4().hex
        self.active = bool(random.getrandbits(1))
        self.name = faker.company()

    def attributes(self):
        """Returns attributes"""
        return {
            "resourceType:": "Patient",
            "identifier:": "[{ Identifier }], // C? Identifies this organization  across multiple systems",
            "active:": "<boolean>, // Whether the organization's record is still in active use",
            "name:": "'<string>', // C? Name used for the organization",
        }
