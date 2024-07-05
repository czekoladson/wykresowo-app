import csv
from django.conf import settings
from earthquakes.models import CityAir
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load data from powietrze file'

    def handle(self, *args, **kwargs):
        # Usuwanie wszystkich istniejących wpisów w CityAir
        if CityAir.objects.count() > 0:
            CityAir.objects.all().delete()

        # Ścieżka do pliku z danymi
        DATA_FILE = settings.BASE_DIR / 'data' / 'powietrze.csv'
        assert DATA_FILE.exists(), f"File {DATA_FILE} does not exist"

        with open(DATA_FILE, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            db_rows = []
            for row in reader:
                db_rows.append(CityAir(
                    city=row['city'],
                    airquality=row['airquality'],
                ))

            # Wstawienie rekordów do bazy danych w partiach po 1000
            CityAir.objects.bulk_create(db_rows, batch_size=1000)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
