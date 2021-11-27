import random
import uuid

from common.base import Base
from resources.practitioner import Practitioner


class Schedule(Base):
    """Schedule

    https://www.hl7.org/fhir/schedule.html

    A container for slots of time that may be available for booking appointments.

    Attributes:
      "resourceType" : "Schedule",
      // from Resource: id, meta, implicitRules, and language
      // from DomainResource: text, contained, extension, and modifierExtension
      "identifier" : [{ Identifier }], // External Ids for this item
      "active" : <boolean>, // Whether this schedule is in active use
      "serviceCategory" : [{ CodeableConcept }], // High-level category
      "serviceType" : [{ CodeableConcept }], // Specific service
      "specialty" : [{ CodeableConcept }], // Type of specialty needed
      "actor" : [{ Reference(Patient|Practitioner|PractitionerRole|RelatedPerson|
       Device|HealthcareService|Location) }], // R!  Resource(s) that availability information is being provided for
      "planningHorizon" : { Period }, // Period of time covered by schedule
      "comment" : "<string>" // Comments on availability
    """

    def __init__(self, faker):
        """Init Schedule Resource"""
        self.resourceType = "Schedule"
        self.actor = Practitioner(faker, sex="male").serialize()

    def attributes(self):
        """Returns attributes"""
        return {
            "resourceType:": "Schedule",
            "identifier": "[{ Identifier }], // External Ids for this item",
            "actor": "[{ Reference(Patient|Practitioner|PractitionerRole|RelatedPerson|Device|HealthcareService|Location) }]",
        }
