import math

from django.contrib.auth.models import User
from django.db import models

from .constants import ACTION_STATUS


class Resource(models.Model):
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
    @property
    def urgency_score(self):
        """
        Drink > Medicine = Food.
        Ideally these would be well defined - exponential decay or reciprical - functions
        """
        score = 0
        if self.drink_days_remaining < 4:
            score += 4 * math.exp(-self.drink_days_remaining)
        
        if self.medicine_days_remaining < 4:
            score += 3 * math.exp(-self.medicine_days_remaining)

        if self.food_days_remaining < 4:
            score += 3 * math.exp(-self.food_days_remaining)

        return score

    @property
    def action_status(self):
        if self.drink_days_remaining < 1 or self.food_days_remaining < 1 or self.medicine_days_remaining < 1:
            return self.action_str(ACTION_STATUS[2])
        
        if self.drink_days_remaining < 3 or self.food_days_remaining < 3 or self.medicine_days_remaining < 3:
            return self.action_str(ACTION_STATUS[1])
        
        return self.action_str(ACTION_STATUS[0])
    
    def action_str(self, action_components):
        return '{} ({})'.format(action_components[0], action_components[1])
    
    def __str__(self):
        return '{}: {}'.format(self.user.username, self.action_status)
