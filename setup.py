from setuptools import setup
from pathlib import Path

setup(
    name="fhir_faker",
    version="0.0.8",
    description="A library for generating fake FHIR resources and data types.",
    long_description="A library for generating fake FHIR resources and data types.",
    keywords="python, fhir, resources, faker",
    author="Kalinin Dmitry <kalinin.mitko@gmail.com>",
    url="https://github.com/null-none/fhir-faker",
    license="MIT",
    packages=["src"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=[
        "Faker==9.8.1",
    ],
)
