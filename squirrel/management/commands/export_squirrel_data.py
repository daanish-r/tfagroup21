from django.core.management.base import BaseCommand,CommandError
from squirrel.models import Fields

class Command(BaseCommand):
    help='This file exports the csv file'

    def add_arguments(self,path):
        path.add_argument('csv_file',nargs='+',type=str)

    def handle(self,*arg,**options):
        import csv
        from django.http import HttpResponse
        path=str(options['csv_file'][0])
        with open(path,'w') as f:
            writer = csv.writer(f)
            header=['Latitude',
                    'Longitude',
                    'Unique_Squirrel_ID',
                    'Shift',
                    'Date',
                    'AGE',
                    'PRIMARY_FUR_COLOR',
                    'Location',
                    'Specific_Location',
                    'Running',
                    'Chasing',
                    'Climbing',
                    'Eating',
                    'Foraging',
                    'Other_Activities',
                    'Kuks',
                    'Quaas',
                    'Moans',
                    'Tail_flags',
                    'Tail_twitches',
                    'Approaches',
                    'Indifferent',
                    'Runs_from',]
            writer.writerow(header)
            #writing data
            squirrel_data = Fields.objects.all()
            for row in squirrel_data:
                writer.writerow([row.Latitude,
                                 row.Longitude,
                                 row.Unique_Squirrel_ID,
                                 row.Shift,
                                 row.Date,
                                 row.AGE,
                                 row.PRIMARY_FUR_COLOR,
                                 row.Location,
                                 row.Specific_Location,
                                 row.Running,
                                 row.Chasing,
                                 row.Climbing,
                                 row.Eating,
                                 row.Foraging,
                                 row.Other_Activities,
                                 row.Kuks,
                                 row.Quaas,
                                 row.Moans,
                                 row.Tail_flags,
                                 row.Tail_twitches,
                                 row.Approaches,
                                 row.Indifferent,
                                 row.Runs_from,])
