from django import forms
from .models import Pers

class CreatPers(forms.ModelForm):
    class Meta:
        model = Pers 
        fields = ['first_name','last_name','mle','grade','tel']