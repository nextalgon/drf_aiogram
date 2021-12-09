from django.db import models


class Words(models.Model):
    GENDERS = [
        ('мужской', 'Muj'),
        ('женский', 'Jen'),
        ('средный', 'Sre')
    ]
    words = models.CharField(verbose_name='So\'zlar', max_length=100)
    gender = models.CharField(verbose_name='Rot', max_length=10, choices=GENDERS)

    def __str__(self):
        return f'{self.gender} {self.words}'
