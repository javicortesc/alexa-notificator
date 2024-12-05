from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Modelo de las Flags
class Flag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) # Nombre de la flag ej "en el transporte publico"
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.name} - {'Active' if self.is_active else 'Inactive'}"

# Define some flag types
FLAG_TYPES = [
    "Using Public Transport",
    "Already Ate",
    "On the Way",
    # Add more as needed
]

@receiver(post_save, sender=User)
def create_user_flags(sender, instance, created, **kwargs):
    if created:
        for flag_name in FLAG_TYPES:
            Flag.objects.create(user=instance, name=flag_name)