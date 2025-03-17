from django import forms

class BirthDateForm(forms.Form):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}),label = 'Date of Birth')
    