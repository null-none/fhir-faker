import random
import uuid
from datetime import date

from ..common.base import Base


class ChargeItem(Base):
    """ChargeItem

    http://www.hl7.org/fhir/chargeitem.html

    The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons.
    Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.

    Attributes:
      "resourceType" : "ChargeItem",
      // from Resource: id, meta, implicitRules, and language
      // from DomainResource: text, contained, extension, and modifierExtension
      "identifier" : [{ Identifier }], // Business Identifier for item
      "definitionUri" : ["<uri>"], // Defining information about the code of this charge item
      "definitionCanonical" : [{ canonical(ChargeItemDefinition) }], // Resource defining the code of this ChargeItem
      "status" : "<code>", // R!  planned | billable | not-billable | aborted | billed | entered-in-error | unknown
      "partOf" : [{ Reference(ChargeItem) }], // Part of referenced ChargeItem
      "code" : { CodeableConcept }, // R!  A code that identifies the charge, like a billing code
      "subject" : { Reference(Patient|Group) }, // R!  Individual service was done for/to
      "context" : { Reference(Encounter|EpisodeOfCare) }, // Encounter / Episode associated with event
      // occurrence[x]: When the charged service was applied. One of these 3:
      "occurrenceDateTime" : "<dateTime>",
      "occurrencePeriod" : { Period },
      "occurrenceTiming" : { Timing },
      "performer" : [{ // Who performed charged service
        "function" : { CodeableConcept }, // What type of performance was done
        "actor" : { Reference(Practitioner|PractitionerRole|Organization|CareTeam|
        Patient|Device|RelatedPerson) } // R!  Individual who was performing
      }],
      "performingOrganization" : { Reference(Organization) }, // Organization providing the charged service
      "requestingOrganization" : { Reference(Organization) }, // Organization requesting the charged service
      "costCenter" : { Reference(Organization) }, // Organization that has ownership of the (potential, future) revenue
      "quantity" : { Quantity }, // Quantity of which the charge item has been serviced
      "bodysite" : [{ CodeableConcept }], // Anatomical location, if relevant
      "factorOverride" : <decimal>, // Factor overriding the associated rules
      "priceOverride" : { Money }, // Price overriding the associated rules
      "overrideReason" : "<string>", // Reason for overriding the list price/factor
      "enterer" : { Reference(Practitioner|PractitionerRole|Organization|Patient|
       Device|RelatedPerson) }, // Individual who was entering
      "enteredDate" : "<dateTime>", // Date the charge item was entered
      "reason" : [{ CodeableConcept }], // Why was the charged  service rendered?
      "service" : [{ Reference(DiagnosticReport|ImagingStudy|Immunization|
       MedicationAdministration|MedicationDispense|Observation|Procedure|
       SupplyDelivery) }], // Which rendered service is being charged?
      // product[x]: Product charged. One of these 2:
      "productReference" : { Reference(Device|Medication|Substance) },
      "productCodeableConcept" : { CodeableConcept },
      "account" : [{ Reference(Account) }], // Account to place this charge
      "note" : [{ Annotation }], // Comments made about the ChargeItem
      "supportingInformation" : [{ Reference(Any) }] // Further information supporting this charge
    """

    def __init__(self, faker):
        """Init ChargeItem Resource"""
        self.resourceType = "ChargeItem"
        self.id = uuid.uuid4().hex
        self.meta = {
            "versionId": "{}".format(random.randrange(10)),
            "lastUpdated": date.today().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        self.status = (
            random.choice(
                [
                    "planned",
                    "billable",
                    "not-billable",
                    "aborted",
                    "billed",
                    "entered-in-error",
                    "unknown",
                ]
            ),
        )

    def attributes(self):
        """Returns attributes"""
        return {
            "resourceType:": "ChargeItem",
            "identifier:": "[{ Identifier }], // Business Identifier for item",
            "status": "<code>, // R!  planned | billable | not-billable | aborted | billed | entered-in-error | unknown",
        }
