import random
import uuid
from datetime import date

from ..common.base import Base
from ..data_types.human_name import HumanName
from ..data_types.address import Address
from ..data_types.contact_point import ContactPoint
from .organization import Organization


class Patient(Base):
    """Patient

    http://www.hl7.org/fhir/patient.html

    Demographics and other administrative information about an individual or animal receiving care or other health-related services.

    Attributes:
      "resourceType"         : "Patient",
      "identifier"           : [{ Identifier }], // An identifier for this patient
      "active"               : <boolean>, // Whether this patient's record is in active use
      "name"                 : [{ HumanName }], // A name associated with the patient
      "birthDate"            : "<date>", // The date of birth for the individual
      "managingOrganization" : { Reference(Organization) }, // Organization that is the custodian of the patient record
      "telecom"              : [{ ContactPoint }], // A contact detail for the individual
    """

    def __init__(self, faker, sex):
        """Init Patient Resource"""
        self.resourceType = "Patient"
        self.id = uuid.uuid4().hex
        self.meta = {
            "versionId": "{}".format(random.randrange(10)),
            "lastUpdated": date.today().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        self.active = bool(random.getrandbits(1))
        self.name = [HumanName(faker, sex).serialize()]
        self.address = [Address(faker).serialize()]
        self.birthDate = faker.date_of_birth(minimum_age=0, maximum_age=110)
        self.managingOrganization = Organization(faker).serialize()
        self.telecom = [ContactPoint(faker).serialize()]

    def attributes(self):
        """Returns attributes"""
        return {
            "resourceType:": "Patient",
            "identifier:": "[{ Identifier }], // An identifier for this patient",
            "active:": "<boolean>, // Whether this patient's record is in active use",
            "name:": "[{ HumanName }], // A name associated with the patient",
            "birthDate:": "'<date>', // The date of birth for the individual",
            "managingOrganization:": "{ Reference(Organization) }, // Organization that is the custodian of the patient record",
            "telecom": "[{ ContactPoint }], // A contact detail for the individual",
        }
