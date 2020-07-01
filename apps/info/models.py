"""Models for the Info app"""
from django.db import models
from django.contrib.auth import get_user_model

class PointTracker(models.Model):
    """Model for tracking gecko points."""
    gecko_points = models.SmallIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    point_haver = models.ForeignKey(get_user_model(), models.CASCADE)

    def __str__(self):
        return f'{self.point_haver}: points={self.gecko_points}: updated={self.updated_at}'
