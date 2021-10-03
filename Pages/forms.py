from django import forms


class ContactFrom(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Name"})
    )
    email = forms.EmailField(
        max_length=200,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Email"})

    )
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={"placeholder": "Message"}),
        label=""
    )
