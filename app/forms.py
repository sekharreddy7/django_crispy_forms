from django import forms
g=[['male','MALE'],['female','FEMALE']]
class contactforms(forms.Form):
    name=forms.CharField(max_length=100,label='FIRST',label_suffix='NAME',help_text='ENTER FIRST NAME',required=True)
    age=forms.IntegerField(max_value=50)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
