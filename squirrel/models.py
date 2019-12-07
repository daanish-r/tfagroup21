from django.db import models

from django.utils.translation import gettext as _

#Create your models here

class Fields(models.Model):

    Unique_Squirrel_ID  = models.CharField(
            help_text = _('input a unique id'),
            max_length=100,
            unique = True,
            primary_key = True,
         )
    
    Specific_Location  = models.CharField(
            help_text = _('describe its specific location'),
            max_length=300,
         )

    Other_Activities  = models.CharField(
            help_text = _('Other Activities'),
            max_length=300,
         )

    Date = models.DateField(
            help_text = _("input today's date"),
        )

    AM = 'am'
    PM = 'pm'
    
    SHIFT_CHOICES = (
            (AM, 'am'),
            (PM, 'pm'),
        )


    SHIFT = models.CharField(
        help_text = _('choose if it was day or night'),
        max_length = 2,
        choices = SHIFT_CHOICES,
        )

    Juvenile = 'Juvenile'
    Adult = 'Adult'
    NAN = '?'
    
    AGE_CHOICES = (
            (Juvenile, 'Juvenile'),
            (Adult, 'Adult'),
            (NAN, '?'),
        )


    AGE = models.CharField(
        help_text = _('how old do you think the squirrel might be?'),
        max_length = 100,
        choices = AGE_CHOICES,
        null = True,
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
        help_text = _('choose its colour'),
        max_length = 100,
        choices = FUR_CHOICES,
        null = True,
        )

    Above = 'Above'
    Below = 'Below'
    
    LOCATION_CHOICES = (
            (Above, 'Above'),
            (Below, 'Below'),
        )


    LOCATION = models.CharField(
        help_text = _('what is your location'),
        max_length = 100,
        choices = LOCATION_CHOICES,
        null = True,
        )


    Latitude = models.FloatField(
            help_text = ('input the latitude of the sighting'),
            null=True,
            )

    Longitude = models.FloatField(
            help_text = ('input the longitude of the sighting'),
            null=True,
            )
    
    Running = models.BooleanField(
            help_text = ("tick if it is running"),
            default=True,
            )

    Chasing = models.BooleanField(
            help_text = ("tick if it is chasing you"),
            default=True,
            )

    Climbing = models.BooleanField(
            help_text = ("tick if it is climbing up something"),
            default=True,
            )

    Eating = models.BooleanField(
            help_text = ("tick if it is eating something"),
            default=True,
            )

    Foraging = models.BooleanField(
            help_text = ("tick if it is foraging"),
            default=True,
            )

    Kuks = models.BooleanField(
            help_text = ("tick if you hear kuks"),
            default=True,
            )

    Quaas = models.BooleanField(
            help_text = ("tick if you hear quaas"),
            default=True,
            )

    Moans = models.BooleanField(
            help_text = ("tick if you hear moans ;)"),
            default=True,
            )

    Tail_flags = models.BooleanField(
            help_text = ("tick if you see its tail flag"),
            default=True,
            )

    Tail_twitches = models.BooleanField(
            help_text = ("tick if you see its tail twitch"),
            default=True,
            )
    
    Approaches = models.BooleanField(
            help_text = ("tick if it approaches you"),
            default=True,
            )

    Indifferent = models.BooleanField(
            help_text = ("tick if it is indifferent to your presence"),
            default=True,
            )    
    
    Runs_from = models.BooleanField(
            help_text = ("tick if it starts running away from you"),
            default=True,
            )
    
    def __str__(self):
        return self.name

