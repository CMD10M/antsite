from csv import DictReader
from django.core.management import BaseCommand
from loads.models import IntegerPair

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the integer pairs data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from integer_pairs.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if IntegerPair.objects.exists():
            print('integer pair data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading integer pair data")

        # Code to load the data into the database
        for row in DictReader(open('./integer_pairs.csv')):
            pair = IntegerPair(hour=row['hour'], load=row['load'])
            pair.save()