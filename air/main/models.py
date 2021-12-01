from django.db import models


class Chronology(models.Model):
    last_update = models.DateField()
    last_post = models.DateField()
    post_periodicity = models.IntegerField()
    update_periodicity = models.IntegerField()


class Station(models.Model):
    region = models.CharField(max_length=64)
    pollution_percentage = models.DecimalField()
    allowable_rate = models.DecimalField()
    chronology = models.ForeignKey(Chronology, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.region} | {self.pollution_percentage}'
