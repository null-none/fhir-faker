import random

from period import Period
from common.base import Base


class HumanName(Base):
    """HumanName

    https://www.hl7.org/fhir/datatypes.html#humanname

    A name of a human with text, parts and usage information.
    Names may be changed or repudiated. People may have different names in different contexts. Names may be divided into parts of different type that have variable significance depending on context, though the division into parts is not always significant. With personal names, the different parts might or might not be imbued with some implicit meaning; various cultures associate different importance with the name parts and the degree to which systems SHALL care about name parts around the world varies widely.

    Attributes:
        use:   : "<code>" // usual | official | temp | nickname | anonymous | old | maiden
        text   : "<string>", // Text representation of the full name
        family : "<string>", // Family name (often called 'Surname')
        given: : ["<string>"], // Given names (not always 'first'). Includes middle names
        prefix : ["<string>"], // Parts that come before the name
        suffix : ["<string>"], // Parts that come after the name
        period : { Period } // Time period when name was/is in use
    """

    def __init__(self, faker, sex):
        """Init HumanName Data Type"""
        self.use = random.choice(
            [
                "usual",
                "official",
                "temp",
                "nickname",
                "anonymous",
                "old",
                "maiden",
            ]
        )
        self.text = getattr(faker, "name_{}".format(sex))()
        self.family = getattr(faker, "last_name_{}".format(sex))()
        self.given = getattr(faker, "first_name_{}".format(sex))()
        self.prefix = [getattr(faker, "prefix_{}".format(sex))()]
        self.suffix = [getattr(faker, "suffix_{}".format(sex))()]
        self.period = Period(faker).serialize()

    def attributes(self):
        """Returns attributes"""
        return {
            "use:": "'<code>' // usual | official | temp | nickname | anonymous | old | maiden",
            "text": "'<string>', // Text representation of the full name",
            "family": "'<string>', // Family name (often called 'Surname')",
            "given": "['<string>'], // Given names (not always 'first'). Includes middle names",
            "prefix": "['<string>'], // Parts that come before the name",
            "suffix": "['<string>''], // Parts that come after the name",
            "period": "{ Period } // Time period when name was/is in use",
        }
