from django import forms


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Fields is not empty')


class ContactForm(forms.Form):
    topic = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    contact_email = forms.EmailField()
    forcefield = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty",
                                 validators=[should_be_empty])
