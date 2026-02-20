from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from resources.models import Resource

BookingStatus = [
    ('01', 'Confirmé'),
    ('02', 'Annulé')
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
        return f"{self.resource.name} réservé par {self.user.username} du {self.start_at} au {self.end_at}"

    def clean(self):
        """
         Validation pour empêcher les chevauchements.
         """

        # Vérifier que start < end
        if self.start_at >= self.end_at:
            raise ValidationError("La date de début doit être avant la date de fin")
        # Chercher les réservations existantes qui se chevauchent
        overlapping = Booking.objects.filter(
            resource=self.resource,
            status__in=['01'],
            start_at__lte=self.end_at,
            end_at__gte=self.start_at)
        if self.pk:
            overlapping = overlapping.exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("Cette ressource est déjà réservée à ce créneau")
    #appel clean() avant de sauvegarder
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

