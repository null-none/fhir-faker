from patient import Patient
from organization import Organization
from practitioner import Practitioner
from appointment import Appointment
from person import Person

class FakeResources(object):
    def patient(self, sex="male"):
        return Patient(self.faker, sex)

    def organization(self):
        return Organization(self.faker)

    def practitioner(self, sex="male"):
        return Practitioner(self.faker, sex)

    def person(self, sex="male"):
        return Person(self.faker, sex)

    def appointment(self):
        return Appointment(self.faker)