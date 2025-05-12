from django.contrib.auth.models import AbstractUser
from django.db import models

class Utente(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utente_set',
        blank=True,
        help_text='I gruppi a cui appartiene questo utente.',
        verbose_name='gruppi'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utente_set',
        blank=True,
        help_text='Permessi specifici per questo utente.',
        verbose_name='permessi'
    )
    
    bio = models.TextField(blank=True)
    data_registrazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username