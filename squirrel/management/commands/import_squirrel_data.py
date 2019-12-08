from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Fields
import csv
import datetime as dt

class Command(BaseCommand):
    help = 'Import Squirrel Census Data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs = '+', type = str)

    def handle(self, *args, **options):
        path=str(options['csv_file'][0])
        with open(path) as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                for i in ('Running','Chasing','Climbing','Eating','Foraging','Kuks','Quuas','Moans','Tail_flags','Tail_twitches','Approaches','Indifferent', 'Runs_from'):
                        if row[i]=='false':
                            row[i]= False
                        else:
                            row[i]= True
                F = Fields( 
                            Longitude = row['X'],
                            Latitude = row['Y'],
                            Unique_Squirrel_ID = row['Unique Squirrel ID'],
                            SHIFT = row['Shift'],
                            Date = dt.datetime.strptime(row['Date'],'%m%d%Y'),
                            AGE = row['Age'],
                            PRIMARY_FUR_COLOUR = row['Primary Fur Color'],
                            LOCATION = row['Location'],
                            Specific_Location = row['Specific Location'],
                            Running = row['Running'],
                            Chasing = row['Chasing'],
                            Climbing = row['Climbing'],
                            Eating = row['Eating'],
                            Foraging = row['Foraging'],
                            Other_Activities = row['Other Activities'],
                            Kuks = row['Kuks'],
                            Quaas = row['Quaas'],
                            Moans = row['Moans'],
                            Tail_flags = row['Tail flags'],
                            Tail_twitches = row['Tail twitches'],
                            Approaches = row['Approaches'],
                            Indifferent = row['Indifferent'],
                            Runs_from = row['Runs from'],
                           )
                 
                F.save()
