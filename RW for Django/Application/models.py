from django.db import models

class Data(models.Model):
    Name = models.CharField(verbose_name='Name', max_length=100)
    Surname = models.CharField(verbose_name='SecondName', max_length=100)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.Name