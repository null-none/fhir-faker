from .human_name import HumanName
from .period import Period
from .address import Address
from .contact_point import ContactPoint
from .identifier import Identifier


class FakeDateTypes(object):
    def human_name(self, sex="male"):
        return HumanName(self.faker, sex)

    def period(self):
        return Period(self.faker)

    def address(self):
        return Address(self.faker)

    def contact_point(self):
        return ContactPoint(self.faker)

    def identifier(self):
        return Identifier(self.faker)
