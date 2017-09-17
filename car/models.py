from django.db import models


class CarMaker(models.Model):
    car_maker = models.CharField(max_length=65)

    def __str__(self):
        return self.car_maker

    class Meta:
        permissions = (('Can view car_maker', 'can_view_car_maker'),)


class Car(models.Model):
    car_name = models.CharField(max_length=65)
    car_maker = models.ForeignKey(CarMaker)
    year = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.car_name
