from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Fields
import csv
import datetime as dt

class Command(BaseCommand):
    help = 'Import Squirrel Census Data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        for row in data:
                F = Fields()
                try:
                    F.Longitude = row[0]
                    F.Latitude = row[1]
                    F.Unique_Squirrel_ID = row[2]
                    F.SHIFT = row[4]
                    F.Date = dt.datetime.strptime(row[5],'%m%d%Y')
                    F.AGE = row[7]
                    F.PRIMARY_FUR_COLOUR = row[8]
                    F.LOCATION = row[12]
                    F.Specific_Location = row[14]
                    F.Running = row[15]
                    F.Chasing = row[16]
                    F.Climbing = row[17]
                    F.Eating = row[18]
                    F.Foraging = row[19]
                    F.Other_Activities = row[20]
                    F.Kuks = row[21]
                    F.Quuas = row[22]
                    F.Moans = row[23]
                    F.Tail_flags = row[24]
                    F.Tail_twitches = row[25]
                    F.Approaches = row[26]
                    F.Indifferent = row[27]
                    F.Runs_from = row[28]
                except Fields.DoesNotExist:
                    raise CommandError('there is some error')
                F.save()
