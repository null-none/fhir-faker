from faker import Faker
from data_types import FakeDateTypes
from resources import FakeResources


class FakeFHIR(FakeDateTypes, FakeResources):
    def __init__(self, locale=["en_US"]):
        self.faker = Faker(locale)
        self.data_types = [
            "human_name",
            "period",
            "address",
            "identifier",
            "contact_point",
        ]
        self.resources = [
            "patient",
            "organization",
            "practitioner",
            "appointment",
            "person",
        ]
