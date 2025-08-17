from data.data import Person
from faker import Faker
import random


faker_en = Faker('en')
Faker.seed()

def generated_person():
    yield Person(
        gender=random.choice(["mr", "mrs"]),
        name=faker_en.first_name(),
        email=faker_en.email(),
        password=faker_en.password(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        company=faker_en.company(),
        address=faker_en.street_address(),
        address2=faker_en.secondary_address(),
        country=random.choice(["Canada", "United States", "Australia"]),
        state=faker_en.state(),
        city=faker_en.city(),
        zipcode=faker_en.zipcode(),
        mobile=faker_en.phone_number(),
        day=str(random.randint(1, 28)),
        month=str(random.randint(1, 12)),
        year=str(random.randint(1900, 2021)),
    )