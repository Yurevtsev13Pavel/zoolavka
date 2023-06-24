from django import forms


class ZooSearchForm(forms.Form):
    search = forms.CharField(max_length=128)
    



