from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Fields

class Command(BaseCommand):
    help = 'Import CSV'
    
    def add_arguments(self,path):
        path.add_argument('csv_file',nargs='+',type=str)

    def handle(self,*arg,**options):
        import csv
        import datetime
        from  squirrel.models import Fields
        path=str(options['csv_file'][0])
        with open(path) as f:
            data=csv.reader(f)
            next(data)
            counter=0
            for line in data:
                for i in (15,16,17,18,19,21,22,23,24,25,26,27,28):
                    if line[i]=='false':
                        line[i]= False
                    else:
                        line[i]= True
                line[5]=datetime.datetime.strptime(line[5],"%m%d%Y").strftime("%Y-%m-%d")
                sighting= Fields(Latitude=line[1],
                    Longitude=line[0],
                    Unique_Squirrel_ID=line[2],
                    SHIFT=line[4],
                    Date=line[5],
                    AGE=line[7],
                    PRIMARY_FUR_COLOR = line[8],
                    LOCATION=line[12],
                    Specific_Location=line[14],
                    Running=line[15],
                    Chasing=line[16],
                    Climbing=line[17],
                    Eating=line[18],
                    Foraging=line[19],
                    Other_Activities=line[20],
                    Kuks=line[21],
                    Quaas=line[22],
                    Moans=line[23], 
                    Tail_flags=line[24],
                    Tail_twitches=line[25],
                    Approaches=line[26],
                    Indifferent=line[27],
                    Runs_from=line[28],)
                #try:
                sighting.save()
                 #   counter+=1
                #except:
                 #   print(f"there was a problem with line{counter}")
                  #  counter+=1
