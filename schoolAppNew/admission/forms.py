from django import forms
from admission.models import student
class studentModelForm(forms.ModelForm):
    class Meta:
        model = student
        fields= '__all__'

class vendorForm(forms.Form):
    name = forms.CharField()
    adress = forms.CharField()
    contact = forms.CharField()
    item = forms.CharField()
    numberOfItems = forms.IntegerField()
    MRP_Rate = forms.IntegerField()
    
