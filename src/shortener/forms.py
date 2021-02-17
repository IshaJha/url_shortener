from django import forms

class generateURLForm(forms.Form):
    actualURL = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # alwaysValid = forms.BooleanField()
    # alwaysValid = forms.BooleanField(required=True, widget=forms.RadioSelect(choices=YES_NO, attrs={'class': 'form-control', 'lable':'Save Forever'}))