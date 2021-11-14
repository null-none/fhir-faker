from patient import Patient
from organization import Organization


class FakeResources(object):
    def patient(self, sex="male"):
        return Patient(self.faker, sex)

    def organization(self):
        return Organization(self.faker)
