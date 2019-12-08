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
                        F.Longitude = row['X']
                        F.Latitude = row['Y']
                        F.Unique_Squirrel_ID = row['Unique Squirrel ID']
                        F.SHIFT = row['Shift']
                        F.Date = dt.datetime.strptime(row['Date'],'%m%d%Y')
                        F.AGE = row['Age']
                        F.PRIMARY_FUR_COLOUR = row['Primary Fur Color']
                        F.LOCATION = row['Location']
                        F.Specific_Location = row['Specific Location']
                        F.Running = row['Running']
                        F.Chasing = row['Chasing']
                        F.Climbing = row['Climbing']
                        F.Eating = row['Eating']
                        F.Foraging = row['Foraging']
                        F.Other_Activities = row['Other Activities']
                        F.Kuks = row['Kuks']
                        F.Quuas = row['Quaas']
                        F.Moans = row['Moans']
                        F.Tail_flags = row['Tail flags']
                        F.Tail_twitches = row['Tail twitches']
                        F.Approaches = row['Approaches']
                        F.Indifferent = row['Indifferent']
                        F.Runs_from = row['Runs from']
            )
                 
            F.save()
