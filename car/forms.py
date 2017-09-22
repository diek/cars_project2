from django.forms import ModelForm

from .models import Car, CarMaker


class CarForm(ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CarMakerForm(ModelForm):

    class Meta:
        model = CarMaker
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
