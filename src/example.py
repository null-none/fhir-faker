from fake import FakeFHIR

fake = FakeFHIR()
# return resources list
fake = FakeFHIR(locale="it_IT")
print(fake.patient().serialize())
print(fake.address().serialize())