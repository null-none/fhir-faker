from src.fake import FakeFHIR


class TestDataTypes:
    def test_address(self):
        fake = FakeFHIR()
        assert "city" in fake.address().serialize()
        assert "text" in fake.address().serialize()

    def test_human_name(self):
        fake = FakeFHIR()
        assert "family" in fake.human_name().serialize()
        assert "given" in fake.human_name().serialize()

    def test_period(self):
        fake = FakeFHIR()
        assert "start" in fake.period().serialize()
        assert "end" in fake.period().serialize()

    def test_identifier(self):
        fake = FakeFHIR()
        assert "use" in fake.identifier().serialize()
        assert "period" in fake.identifier().serialize()

    def test_contact_point(self):
        fake = FakeFHIR()
        assert "use" in fake.contact_point().serialize()
        assert "value" in fake.contact_point().serialize()
