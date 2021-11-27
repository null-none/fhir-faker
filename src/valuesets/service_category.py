def service_category():
    """ServiceCategory

    https://www.hl7.org/fhir/valueset-service-category.html

    Demographics and other administrative information about an individual or animal receiving care or other health-related services.

    This value set is used in the following places:
        CodeSystem: This value set is the designated 'entire code system' value set for ServiceCategory
        Resource: Appointment.serviceCategory (CodeableConcept / Example)
        Resource: Slot.serviceCategory (CodeableConcept / Example)
        Resource: HealthcareService.category (CodeableConcept / Example)
        Resource: Schedule.serviceCategory (CodeableConcept / Example)
    """
    return [
        {"code": 1, "display": "Adoption", "definition": "Adoption"},
        {
            "code": 7,
            "display": "Community Health Care",
            "definition": "Community Health Care",
        },
        {
            "code": 16,
            "display": "Financial & Material Aid",
            "definition": "Financial & Material Aid",
        },
        {
            "code": 27,
            "display": "Specialist Medical",
            "definition": "Specialist Medical - requires referral",
        },
        {"code": 33, "display": "Transport", "definition": "Transport"},
    ]
