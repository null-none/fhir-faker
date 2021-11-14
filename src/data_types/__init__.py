from human_name import HumanName
from period import Period
from address import Address


class FakeDateTypes(object):
    def human_name(self, sex="male"):
        return HumanName(self.faker, sex)

    def period(self):
        return Period(self.faker)

    def address(self):
        return Address(self.faker)
