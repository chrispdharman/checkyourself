from django.contrib.auth.models import User
from django.db import models


class Resources(models.Model):
    """
    Object intended to capture and monitor the current essential resource accessibility of a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    drink_days_remaining = models.IntegerField(null=False, default=0,
                                               help_text='Days remaining with water access.')

    food_days_remaining = models.IntegerField(null=False, default=0,
                                              help_text='Days remaining with food access.')
    
    medicine_days_remaining = models.IntegerField(null=False, default=0,
                                                  help_text='Days remaining with medicine access.')
    