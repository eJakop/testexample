from .models import Guide
from .models import Type
from django.forms import ModelForm, TextInput, ChoiceField, ModelChoiceField


class GuideForm(ModelForm):

    class Meta:
        model = Guide
        fields = '__all__'

