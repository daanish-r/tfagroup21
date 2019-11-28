from django.db import models

from django.utils.translation import gettext as _

#Create your models here

class Fields(models.Model):

    Unique_Squirrel_ID  = models.CharField(
            help_text = _('Unique squirrel ID'),
            max_length=100,
            unique = True
            primary_key = True
         )
    
    Specific_Location  = models.CharField(
            help_text = _('Specific location of squirrel inside central park'),
            max_length=300,
         )

    Other_Activities  = models.CharField(
            help_text = _('Other Activities'),
            max_length=300,
         )

    Date = models.DateField(
            help_text = _('Date when the squirrel was observed'),
        )

    AM = 'am'
    PM = 'pm'
    
    SHIFT_CHOICES = (
            (AM, 'am'),
            (PM, 'pm'),
        )


    SHIFT = models.CharField(
        help_text = _('shit'),
        max_length = 2,
        choices = SHIFT_CHOICES,
        )

    Juvenile = 'Juvenile'
    Adult = 'Adult'
    ? = '?'
    
    AGE_CHOICES = (
            (Juvenile, 'Juvenile'),
            (Adult, 'Adult'),
            (?, '?'),
        )


    AGE = models.CharField(
        help_text = _('Age of the squirrel'),
        max_length = 100,
        choices = AGE_CHOICES,
        null = True
        )

    Grey = 'Grey'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    
    FUR_CHOICES = (
            (Grey, 'Grey'),
            (Cinnamon, 'Cinnamon'),
            (Black, 'Black'),
        )


    PRIMARY_FUR_COLOR = models.CharField(
        help_text = _('Primary fur color of the squirrel'),
        max_length = 100,
        choices = FUR_CHOICES,
        null = True
        )

    Above = 'Above'
    Below = 'Below'
    
    LOCATION_CHOICES = (
            (Above, 'Above'),
            (Below, 'Below'),
        )


    LOCATION = models.CharField(
        help_text = _('Locatrion of the squirrel'),
        max_length = 100,
        choices = LOCATION_CHOICES,
        null = True
        )


    Latitude = models.IntegerField(
            help_text = ('Latitude of the sighting')
            null=True
            )

    Longitude = models.IntegerField(
            help_text = ('Longitude of the sighting')
            null=True
            )
    
    Running = models.BooleanField(default=True)
    Chasing = models.BooleanField(default=True)
    Climbing = models.BooleanField(default=True)
    Eating = models.BooleanField(default=True)
    Foraging = models.BooleanField(default=True)
    Kuks = models.BooleanField(default=True)
    Quaas = models.BooleanField(default=True)
    Moans = models.BooleanField(default=True)
    Tail_flags = models.BooleanField(default=True)
    Tail_twitches = models.BooleanField(default=True)
    Approaches  = models.BooleanField(default=True)
    Indifferent = models.BooleanField(default=True)
    Runs_from = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name

