def service_type():
    """ServiceType

    https://www.hl7.org/fhir/valueset-service-type.html

    Demographics and other administrative information about an individual or animal receiving care or other health-related services.

    This value set is used in the following places:
        CodeSystem: This value set is the designated 'entire code system' value set for ServiceType
        Resource: Appointment.serviceType (CodeableConcept / Example)
        Resource: Slot.serviceType (CodeableConcept / Example)
        Resource: Encounter.serviceType (CodeableConcept / Example)
        Resource: HealthcareService.type (CodeableConcept / Example)
        Resource: Schedule.serviceType (CodeableConcept / Example)
    """
    return [
        {
            "code": 1,
            "display": "Adoption/Permanent Care Info/Support",
            "definition": "Adoption & permanent care information/support",
        },
        {
            "code": 9,
            "display": "Home Maintenance and Repair",
            "definition": "Home maintenance and repair",
        },
        {"code": 63, "display": "Osteopathy", "definition": "Osteopathy"},
        {"code": 109, "display": "Pharmacotherapy", "definition": "Pharmacotherapy"},
    ]
