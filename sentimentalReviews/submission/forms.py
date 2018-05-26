from django import forms

class Review (forms.Form):
    review = forms.CharField(label = '', max_length = 300, widget =forms.Textarea(attrs={'rows': 15, 'cols': 100}))

