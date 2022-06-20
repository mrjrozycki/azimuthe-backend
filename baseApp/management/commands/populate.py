from django.core.management.base import BaseCommand, CommandError

from baseApp.models import *
from faker import Faker

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **options):
        faker = Faker()
        for _ in range(50):
            warehouse = Warehouse.objects.create(
                name=faker.company(),
                city=faker.city(),
                street=faker.street_name(),
                zipcode=faker.postcode(),
                country=faker.country()
            )
            for _ in range(10):
                product = Product.objects.create(
                    name=faker.word(),
                    stock=faker.random_int(min=0, max=1000),
                    warehouse=warehouse
                )
