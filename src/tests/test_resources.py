from src.fake import FakeFHIR


class TestResources:
    def test_organization(self):
        fake = FakeFHIR()
        assert "resourceType" in fake.organization().serialize()
        assert "name" in fake.organization().serialize()

    def test_patient(self):
        fake = FakeFHIR()
        assert "resourceType" in fake.patient(sex="male").serialize()
        assert "name" in fake.patient(sex="male").serialize()

    def test_practitioner(self):
        fake = FakeFHIR()
        assert "resourceType" in fake.practitioner(sex="female").serialize()
        assert "name" in fake.practitioner(sex="female").serialize()

    def test_appointment(self):
        fake = FakeFHIR()
        assert "resourceType" in fake.appointment().serialize()

    def test_person(self):
        fake = FakeFHIR()
        assert "resourceType" in fake.person().serialize()

    def test_schedule(self):
        fake = FakeFHIR()
        assert "actor" in fake.schedule().serialize()

    def test_slot(self):
        fake = FakeFHIR()
        assert "status" in fake.slot().serialize()
        assert "start" in fake.slot().serialize()
        assert "end" in fake.slot().serialize()