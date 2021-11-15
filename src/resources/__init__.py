from patient import Patient
from organization import Organization
from practitioner import Practitioner


class FakeResources(object):
    def patient(self, sex="male"):
        return Patient(self.faker, sex)

    def organization(self):
        return Organization(self.faker)

    def practitioner(self, sex="male"):
        return Practitioner(self.faker, sex)
