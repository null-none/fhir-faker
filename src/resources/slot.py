import random
import uuid
from datetime import date, timedelta

from common.base import Base
from resources.schedule import Schedule


class Slot(Base):
    """Slot

    https://www.hl7.org/fhir/slot.html

    A container for slots of time that may be available for booking appointments.

    Attributes:
      "resourceType" : "Slot",
      // from Resource: id, meta, implicitRules, and language
      // from DomainResource: text, contained, extension, and modifierExtension
      "identifier" : [{ Identifier }], // External Ids for this item
      "serviceCategory" : [{ CodeableConcept }], // A broad categorization of the service that is to be performed during this appointment
      "serviceType" : [{ CodeableConcept }], // The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource
      "specialty" : [{ CodeableConcept }], // The specialty of a practitioner that would be required to perform the service requested in this appointment
      "appointmentType" : { CodeableConcept }, // The style of appointment or patient that may be booked in the slot (not service type)
      "schedule" : { Reference(Schedule) }, // R!  The schedule resource that this slot defines an interval of status information
      "status" : "<code>", // R!  busy | free | busy-unavailable | busy-tentative | entered-in-error
      "start" : "<instant>", // R!  Date/Time that the slot is to begin
      "end" : "<instant>", // R!  Date/Time that the slot is to conclude
      "overbooked" : <boolean>, // This slot has already been overbooked, appointments are unlikely to be accepted for this time
      "comment" : "<string>" // Comments on the slot to describe any extended information. Such as custom constraints on the slot
    """

    def __init__(self, faker):
        """Init Slot Resource"""
        self.resourceType = "Slot"
        self.schedule = Schedule(faker).serialize()
        self.status = random.choice(
            ["busy", "free", "busy-unavailable", "busy-tentative", "entered-in-error"]
        )
        self.start = date.today().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.end = (date.today() + timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

    def attributes(self):
        """Returns attributes"""
        return {
            "resourceType:": "Slot",
            "identifier": "[{ Identifier }], // External Ids for this item",
            "schedule": "{ Reference(Schedule) }, // R!  The schedule resource that this slot defines an interval of status information",
            "status": "<code>, // R!  busy | free | busy-unavailable | busy-tentative | entered-in-error",
            "start": "<instant>, // R!  Date/Time that the slot is to begin",
            "end": "<instant>, // R!  Date/Time that the slot is to conclude",
        }
