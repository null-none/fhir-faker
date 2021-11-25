import random
import uuid
from datetime import date

from ..common.base import Base
from ..data_types.human_name import HumanName
from ..data_types.address import Address
from ..data_types.contact_point import ContactPoint


class Practitioner(Base):
    """Practitioner

    https://www.hl7.org/fhir/practitioner.html

    Demographics and other administrative information about an individual or animal receiving care or other health-related services.

    Attributes:
      "resourceType" : "Practitioner",
      "identifier"   : [{ Identifier }], // An identifier for the person as this agent
      "active"       : <boolean>, // Whether this practitioner's record is in active use
      "name"         : [{ HumanName }], // The name(s) associated with the practitioner
      "telecom"      : [{ ContactPoint }], // A contact detail for the practitioner (that apply to all roles)
      "address"      : [{ Address }], // Address(es) of the practitioner that are not role specific (typically home address)
      "gender"       : "<code>", // male | female | other | unknown
      "birthDate"    : "<date>", // The date  on which the practitioner was born
      "telecom"      : [{ ContactPoint }], // A contact detail for the individual
    """

    def __init__(self, faker, sex):
        """Init Practitioner Resource"""
        self.id = uuid.uuid4().hex
        self.meta = {
            "versionId": "{}".format(random.randrange(10)),
            "lastUpdated": date.today().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        self.resourceType = "Practitioner"
        self.active = bool(random.getrandbits(1))
        self.name = [HumanName(faker, sex).serialize()]
        self.address = [Address(faker).serialize()]
        self.birthDate = faker.date_of_birth(minimum_age=0, maximum_age=110)
        self.gender = faker.name()
        self.telecom = [ContactPoint(faker).serialize()]

    def attributes(self):
        """Returns attributes"""
        return {
            "resourceType:": "Practitioner",
            "identifier": "[{ Identifier }], // An identifier for the person as this agent",
            "active": "<boolean>, // Whether this practitioner's record is in active use",
            "name": "[{ HumanName }], // The name(s) associated with the practitioner",
            "telecom": "[{ ContactPoint }], // A contact detail for the practitioner (that apply to all roles)",
            "address": "[{ Address }], // Address(es) of the practitioner that are not role specific (typically home address)",
            "gender": "'<code>', // male | female | other | unknown",
            "birthDate": "'<date>', // The date  on which the practitioner was born",
            "telecom": "[{ ContactPoint }], // A contact detail for the individual",
        }
