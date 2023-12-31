from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=5, max_length=255)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=355)