from django import forms
from webproject.settings import LOREM

class CssForm(forms.Form):
    paragraph_text = forms.CharField(label='Text for paragraph', max_length=200, required=False, initial=LOREM)
    text_color = forms.CharField(label='Text color', max_length=20)
    background_color = forms.CharField(label='Background color', max_length=20)

class TableForm(forms.Form):
    rows = forms.IntegerField(label='Number of Rows', min_value=1, initial=1)
