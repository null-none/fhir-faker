from src.fake import FakeFHIR


class TestResources:
    def test_organization(self):
        fake = FakeFHIR()
        assert "resourceType" in fake.organization().serialize()
        assert "name" in fake.organization().serialize()

    def test_patient(self):
        fake = FakeFHIR()
        assert "resourceType" in fake.patient().serialize()
        assert "name" in fake.patient().serialize()

    def test_patient(self):
        fake = FakeFHIR()
        assert "resourceType" in fake.practitioner().serialize()
        assert "name" in fake.practitioner().serialize()
