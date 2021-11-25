import random
import uuid
from datetime import date

from ..common.base import Base
from ..data_types.human_name import HumanName
from ..data_types.address import Address
from ..data_types.contact_point import ContactPoint
from .organization import Organization


class Person(Base):
    """Person

      http://www.hl7.org/fhir/person.html

      Demographics and administrative information about a person independent of a specific health-related context.

      Attributes:
        "resourceType"         : "Person",
    "identifier" : [{ Identifier }], // A human identifier for this person
    "name" : [{ HumanName }], // A name associated with the person
    "telecom" : [{ ContactPoint }], // A contact detail for the person
    "gender" : "<code>", // male | female | other | unknown
    "birthDate" : "<date>", // The date on which the person was born
    "address" : [{ Address }], // One or more addresses for the person
    "photo" : { Attachment }, // Image of the person
    "managingOrganization" : { Reference(Organization) }, // The organization that is the custodian of the person record
    "active" : <boolean>, // This person's record is in active use
    "link" : [{ // Link to a resource that concerns the same actual person
      "target" : { Reference(Patient|Practitioner|RelatedPerson|Person) }, // R!  The resource to which this actual person is associated
      "assurance" : "<code>" // level1 | level2 | level3 | level4
    }]
    """

    def __init__(self, faker, sex):
        """Init Person Resource"""
        self.resourceType = "Person"
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
