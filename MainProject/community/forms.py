from django.forms import ModelForm
from .models import Motive


class CreateMotiveForm(ModelForm):
    class Meta:
        model = Motive
        exclude = ['id','created_at','updated_at']
        