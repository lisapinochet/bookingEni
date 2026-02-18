from django.contrib.auth.models import User
from django.db import models

from resources.models import Resource

BookingStatus = [
    ('01', 'En attente de confirmation'),
    ('02', 'Confirmée'),
    ('03', 'Annulé')
]
# Create your models here.
class Booking(models.Model):
    start_at = models.DateField()
    end_at = models.DateField()
    status = models.CharField(max_length=10, choices=BookingStatus, default='01')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    def __str__(self):
        return f" Réservation de {self.resource.name} du {self.start_at} au {self.end_at} | {self.status} | créé le : {self.created_at} par {self.user}"