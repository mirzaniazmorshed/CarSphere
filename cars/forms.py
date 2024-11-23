from django import forms

from cars.models import CarModel, CommentModel
class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'email', 'body']
        