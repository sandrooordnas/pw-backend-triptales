from django.db import models
from utenti.models import Utente

class Gruppo(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    creatore = models.ForeignKey(Utente, on_delete=models.CASCADE)
    membri = models.ManyToManyField(Utente, related_name='gruppi_iscritti')

class Post(models.Model):
    testo = models.TextField()
    foto_url = models.URLField(blank=True)
    latitudine = models.FloatField(blank=True, null=True)
    longitudine = models.FloatField(blank=True, null=True)
    data_creazione = models.DateTimeField(auto_now_add=True)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)

class Commento(models.Model):
    testo = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)