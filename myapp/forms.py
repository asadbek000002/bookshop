from django import forms
from .models import Buy
from users.models import Saved

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ['kitob', 'user']
        fields = '__all__'


class ChoiceForms(forms.ModelForm):
    class Meta:
        model = Saved
        exclude = ['book', 'yaratilgan_vaqt']
        fields = '__all__'