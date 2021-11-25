import random
import uuid
from datetime import date, timedelta

from common.base import Base
from data_types.human_name import HumanName
from data_types.address import Address
from resources.practitioner import Practitioner
from data_types.contact_point import ContactPoint


class Appointment(Base):
    """Appointment

    http://www.hl7.org/fhir/appointment.html

    A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).

    Attributes:
      "resourceType" : "Appointment",
      // from Resource: id, meta, implicitRules, and language
      // from DomainResource: text, contained, extension, and modifierExtension
      "identifier" : [{ Identifier }], // External Ids for this item
      "status" : "<code>", // R!  proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
      "cancelationReason" : { CodeableConcept }, // The coded reason for the appointment being cancelled
      "serviceCategory" : [{ CodeableConcept }], // A broad categorization of the service that is to be performed during this appointment
      "serviceType" : [{ CodeableConcept }], // The specific service that is to be performed during this appointment
      "specialty" : [{ CodeableConcept }], // The specialty of a practitioner that would be required to perform the service requested in this appointment
      "appointmentType" : { CodeableConcept }, // The style of appointment or patient that has been booked in the slot (not service type)
      "reasonCode" : [{ CodeableConcept }], // Coded reason this appointment is scheduled
      "reasonReference" : [{ Reference(Condition|Procedure|Observation|
       ImmunizationRecommendation) }], // Reason the appointment is to take place (resource)
      "priority" : "<unsignedInt>", // Used to make informed decisions if needing to re-prioritize
      "description" : "<string>", // Shown on a subject line in a meeting request, or appointment list
      "supportingInformation" : [{ Reference(Any) }], // Additional information to support the appointment
      "start" : "<instant>", // When appointment is to take place
      "end" : "<instant>", // When appointment is to conclude
      "minutesDuration" : "<positiveInt>", // Can be less than start/end (e.g. estimate)
      "slot" : [{ Reference(Slot) }], // The slots that this appointment is filling
      "created" : "<dateTime>", // The date that this appointment was initially created
      "comment" : "<string>", // Additional comments
      "patientInstruction" : "<string>", // Detailed information and instructions for the patient
      "basedOn" : [{ Reference(ServiceRequest) }], // The service request this appointment is allocated to assess
      "participant" : [{ // R!  Participants involved in appointment
        "type" : [{ CodeableConcept }], // Role of participant in the appointment
        "actor" : { Reference(Patient|Practitioner|PractitionerRole|RelatedPerson|
        Device|HealthcareService|Location) }, // Person, Location/HealthcareService or Device
        "required" : "<code>", // required | optional | information-only
        "status" : "<code>", // R!  accepted | declined | tentative | needs-action
        "period" : { Period } // Participation period of the actor
      }],
      "requestedPeriod" : [{ Period }] // Potential date/time interval(s) requested to allocate the appointment within
    """

    def __init__(self, faker):
        """Init Appointment Resource"""
        self.resourceType = "Appointment"
        self.identifier = uuid.uuid4().hex
        self.status = random.choice(
            [
                "proposed",
                "pending",
                "booked",
                "arrived",
                "fulfilled",
                "cancelled",
                "noshow",
                "entered-in-error",
                "checked-in",
                "waitlist",
            ]
        )
        self.priority = 1
        self.start = date.today().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.end = (date.today() + timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.participant = [
            {
                "status": random.choice(
                    [
                        "accepted",
                        "declined",
                        "tentative",
                        "needs-action"
                    ]
                ),
                "actor": Practitioner(faker, sex="male").serialize(),
            }
        ]

    def attributes(self):
        """Returns attributes"""
        return {
            "resourceType:": "Appointment",
            "identifier:": "[{ Identifier }], // An identifier for this patient",
            "status": "'<code>', // R!  proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist",
            "priority": "'<unsignedInt>', // Used to make informed decisions if needing to re-prioritize",
            "start": "<instant>, // When appointment is to take place",
            "end": "<instant>, // When appointment is to conclude",
            "participant": {
                "status": "<code>, // R!  accepted | declined | tentative | needs-action",
                "actor": "{ Reference(Patient|Practitioner|PractitionerRole|RelatedPerson|Device|HealthcareService|Location) }, // Person, Location/HealthcareService or Device",
            },
        }
