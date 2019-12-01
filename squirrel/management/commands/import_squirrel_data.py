from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Fields
import csv
import datetime as dt

class Command(BaseCommand):
    help = 'Import Squirrel Census Data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str, help='The CSV file to be imported')

    def handle(self,*args, **options):

        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            next(dataReader)

            for row in dataReader:
                F = Fields()

                try:
                    F.longitude = row[0]
                    F.latitude = row[1]
                    F.unique_squirrel_id = row[2]
                    F.shift = row[4]
                    F.date = dt.datetime.strptime(row[5],'%m%d%Y')
                    F.age = row[7]
                    F.primary_fur_color = row[8]
                    F.location = row[12]
                    F.specific_location = row[14]
                    F.running = row[15]
                    F.chasing = row[16]
                    F.climbing = row[17]
                    F.eating = row[18]
                    F.foraging = row[19]
                    F.other_activities = row[20]
                    F.kuks = row[21]
                    F.quuas = row[22]
                    F.moans = row[23]
                    F.tail_flags = row[24]
                    F.tail_twitches = row[25]
                    F.approaches = row[26]
                    F.indifferent = row[27]
                    F.runs_from = row[28]

                except Fields.DoesNotExist:
                    raise CommandError('there is some error')

                F.save()
