from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES =(
    ('S','Stripe'),
    ('P','PayPal'),
)

class CheckoutForm(forms.Form):
    add_1 = forms.CharField()
    add_2 = forms.CharField(required=False)
    country = CountryField(blank_label='(Select Country)').formfield()
    #state = forms.CharField()
    zip = forms.CharField()
    same_bill = forms.BooleanField(widget = forms.CheckboxInput(),required = False)
    save_info = forms.BooleanField(widget = forms.CheckboxInput(),required = False)
    payment_option = forms.ChoiceField(widget = forms.RadioSelect,choices = PAYMENT_CHOICES)
