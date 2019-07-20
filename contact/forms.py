from django import forms

class ContactForm(forms.Form):
    lastname = forms.CharField(required=True)
    firstname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=False)
    phone = forms.CharField(required=False)

class UploadFileForm(forms.Form):
    title = forms.CharField(required=False, max_length=50)
    file = forms.FileField(required=True)
