from django import forms
from django.contrib.auth.models import User
# from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm


SOLUTION_CHOICES = (
    ('S', 'Startup'),
    ('I', 'Investor')
)
class CustomSignupForm(UserCreationForm):

    label = forms.ChoiceField(widget=forms.RadioSelect, choices=SOLUTION_CHOICES)
    def custom_signup(self, request, user):
        custom_form = self #use local signup()
        if hasattr(custom_form, 'signup') and callable(custom_form.signup):
            custom_form.signup(request, user)

    def signup(self, request, user):
        up = user.profile
        up.label = self.cleaned_data["label"]
        
        user.save()
        up.save()

       
        # PAYMENT_CHOICES = (
#     ('S', 'Stripe'),
#     ('P', 'PayPal')
# )


# class CheckoutForm(forms.Form):
#     shipping_address = forms.CharField(required=False)
#     shipping_address2 = forms.CharField(required=False)
#     shipping_country = CountryField(blank_label='(select country)').formfield(
#         required=False,
#         widget=CountrySelectWidget(attrs={
#             'class': 'custom-select d-block w-100',
#         }))
#     shipping_zip = forms.CharField(required=False)

#     billing_address = forms.CharField(required=False)
#     billing_address2 = forms.CharField(required=False)
#     billing_country = CountryField(blank_label='(select country)').formfield(
#         required=False,
#         widget=CountrySelectWidget(attrs={
#             'class': 'custom-select d-block w-100',
#         }))
#     billing_zip = forms.CharField(required=False)

#     same_billing_address = forms.BooleanField(required=False)
#     set_default_shipping = forms.BooleanField(required=False)
#     use_default_shipping = forms.BooleanField(required=False)
#     set_default_billing = forms.BooleanField(required=False)
#     use_default_billing = forms.BooleanField(required=False)

#     payment_option = forms.ChoiceField(
#         widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


# class CouponForm(forms.Form):
#     code = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Promo code',
#         'aria-label': 'Recipient\'s username',
#         'aria-describedby': 'basic-addon2'
#     }))


# class RefundForm(forms.Form):
#     ref_code = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea(attrs={
#         'rows': 4
#     }))
#     email = forms.EmailField()


# class PaymentForm(forms.Form):
#     stripeToken = forms.CharField(required=False)
#     save = forms.BooleanField(required=False)
#     use_default = forms.BooleanField(required=False)
