# fhir-faker
A library for generating fake FHIR resources and datatypes

#### Install 
```bash
pip install fhir-faker
```

#### Examples

```python
# Data types

from fhir_faker.fake import FakeFHIR

fake = FakeFHIR()

# return data types list
print(fake.data_types)
# ['human_name', 'period', 'address']

# return HumanName data type
print(fake.human_name().serialize())
# {'use': 'anonymous', 'suffix': [u'MD'], 'family': u'Walters', 'text': u'Edward Smith', 'given': u'David', 'period': {'start': datetime.date(2009, 2, 1), 'end': datetime.date(2021, 11, 14)}, 'prefix': [u'Mr.']}


# return HumanName attributes
print(fake.human_name().attributes())
# {'given': "['<string>'], // Given names (not always 'first'). Includes middle names", 'suffix': "['<string>''], // Parts that come after the name", 'family': "'<string>', // Family name (often called 'Surname')", 'text': "'<string>', // Text representation of the full name", 'period': '{ Period } // Time period when name was/is in use', 'prefix': "['<string>'], // Parts that come before the name", 'use:': "'<code>' // usual | official | temp | nickname | anonymous | old | maiden"}


# update key value data for HumanName data type
print(fake.human_name().update({"use": "temp"}))
# {'use': 'temp', 'suffix': [u'MD'], 'family': u'Williams', 'text': u'Anthony Adams', 'given': u'Michael', 'period': {'start': datetime.date(1967, 7, 12), 'end': datetime.date(2021, 11, 14)}, 'prefix': [u'Mr.']}

```


```python
# Resources

from fhir_faker.fake import FakeFHIR

fake = FakeFHIR()
# return resources list
print(fake.resources)
# ["patient", "organization"]

# return Patient resource
print(fake.patient().serialize())
# {'managingOrganization': {'resourceType': 'Organization', 'active': False, 'identifier': '745fba5058bf4351abbe02e8f4276365', 'name': u'Glenn Group'}, 'name': [{'use': 'maiden', 'suffix': [u'Jr.'], 'family': u'Sanford', 'text': u'Matthew Todd PhD', 'given': u'Gary', 'period': {'start': datetime.date(2000, 6, 18), 'end': datetime.date(2021, 11, 14)}, 'prefix': [u'Dr.']}], 'resourceType': 'Patient', 'birthDate': datetime.date(1993, 8, 24), 'address': [{'city': u'Johnsonside', 'use': 'temp', 'district': u'bury', 'text': u'PSC 1292, Box 4906\nAPO AE 46449', 'period': {'start': datetime.date(1988, 12, 9), 'end': datetime.date(2021, 11, 14)}, 'state': u'haven', 'country': u'Congo', 'postalCode': u'41762', 'line': [u'6676 Lisa Fords Suite 341'], 'type': 'both'}], 'active': True, 'identifier': 'ec558e77780048608cefdab7f8f0c0e7'}

# return Patient resource
print(fake.patient(sex="male").serialize())
# {'managingOrganization': {'resourceType': 'Organization', 'active': True, 'identifier': 'ec4c3594b0af49008b1f674dc5e59c8f', 'name': u'Ramirez-Lowe'}, 'name': [{'use': 'maiden', 'suffix': [u'Jr.'], 'family': u'Rivers', 'text': u'Carlos Ruiz', 'given': u'Joseph', 'period': {'start': datetime.date(2008, 1, 28), 'end': datetime.date(2021, 11, 14)}, 'prefix': [u'Mr.']}], 'resourceType': 'Patient', 'birthDate': datetime.date(1919, 4, 5), 'address': [{'city': u'East Kristinaburgh', 'use': 'billing', 'district': u'side', 'text': u'081 Lawrence Street Suite 400\nJessicaton, NE 41331', 'period': {'start': datetime.date(1989, 8, 13), 'end': datetime.date(2021, 11, 14)}, 'state': u'haven', 'country': u'Dominica', 'postalCode': u'31375', 'line': [u'142 Tiffany Cliff'], 'type': 'physical'}], 'active': True, 'identifier': '981a82f2cbc3438a8427093ac4209542'}

# return Patient resource
print(fake.patient(sex="female").serialize())
# {'managingOrganization': {'resourceType': 'Organization', 'active': False, 'identifier': 'b37d040b05104033bfda2502737f9763', 'name': u'Hogan, Clark and Lee'}, 'name': [{'use': 'maiden', 'suffix': [u'MD'], 'family': u'Hines', 'text': u'Kara York', 'given': u'Jennifer', 'period': {'start': datetime.date(2014, 2, 28), 'end': datetime.date(2021, 11, 14)}, 'prefix': [u'Mrs.']}], 'resourceType': 'Patient', 'birthDate': datetime.date(2007, 7, 27), 'address': [{'city': u'East Bradley', 'use': 'temp', 'district': u'bury', 'text': u'7683 Monique Square\nSouth Elizabethborough, HI 30811', 'period': {'start': datetime.date(1983, 4, 18), 'end': datetime.date(2021, 11, 14)}, 'state': u'stad', 'country': u'Saint Martin', 'postalCode': u'34715', 'line': [u'196 Megan Trail Suite 418'], 'type': 'physical'}], 'active': True, 'identifier': '3ab6baf23fda449bbbba83098f380753'}

```


```python
# Locale

from fhir_faker.fake import FakeFHIR

fake = FakeFHIR(locale="it_IT")
print(fake.patient().serialize())
# {'managingOrganization': {'resourceType': 'Organization', 'active': True, 'identifier': '5d1890fcd4db404a9df4f3dadeb4f46f', 'name': u'Gadda, Bellucci e Muratori s.r.l.'}, 'name': [{'use': 'maiden', 'suffix': [u''], 'family': u'Ovadia', 'text': u'Sabatino Mastandrea', 'given': u'Pasqual', 'period': {'start': datetime.date(1961, 8, 15), 'end': datetime.date(2021, 11, 14)}, 'prefix': [u'Sig.']}], 'resourceType': 'Patient', 'birthDate': datetime.date(1916, 12, 10), 'address': [{'city': u'Taliani del friuli', 'use': 'work', 'district': u'umbro', 'text': u"Rotonda Sandro 95 Appartamento 70\nDisdero nell'emilia, 38280 Trento (SR)", 'period': {'start': datetime.date(1965, 3, 10), 'end': datetime.date(2021, 11, 14)}, 'state': u'umbro', 'country': u'Somalia', 'postalCode': u'97135', 'line': [u'Borgo Baglioni 2'], 'type': 'both'}], 'active': True, 'identifier': 'c221a4a07fab4202bf2198756bba1966'}
print(fake.address().serialize())
# {'city': u'Borgo Silvia umbro', 'use': 'old', 'district': u'terme', 'text': u'Stretto Pininfarina 076\nEmilio salentino, 86563 Benevento (AO)', 'period': {'start': datetime.date(2014, 3, 19), 'end': datetime.date(2021, 11, 14)}, 'state': u'lido', 'country': u'Italy', 'postalCode': u'48118', 'line': [u'Via Baroffio 9'], 'type': 'both'}
```
