from django import forms
from django.core import validators
from firstapp.models import User

def validate_geeks_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise forms.ValidationError("This field accepts mail id of google only")

def valiate_descrip(value):
    if len(value) < 20 :
        raise forms.ValidationError("Description should be at least 20 words.")
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(validators=[validate_geeks_mail])
    description = forms.CharField(widget=forms.Textarea,validators=[valiate_descrip])
    botcatch = forms.CharField(required=False,widget=forms.HiddenInput)

    def catchbot(self):
        bot = self.cleaned_data['botcatch']
        if len(bot) > 0:
            raise forms.ValidationError("CAUGHT YOU")
        return bot

class NewformPage(forms.ModelForm):
    #def validators can be used here
    # Each model will have its own class meta
    class Meta:
        model = User
        fields = '__all__'
#    fields = ('field1','field2')

