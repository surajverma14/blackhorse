from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from allauth.account.views import SignupView
# from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from .models import ContactForm



def home(request):
    return render(request,'home.html',{})

def contact(request):
	return render(request,'contact-us.html')		


def leadership(request):
	return render(request,'leadership.html')

# def career(request):
# 	return render(request,'index/careers.html')





def contact_form_submission(request):
	if request.method =='POST':

		
		contact_name = request.POST["contact_name"]
		contact_email = request.POST["contact_email"]
		contact_subject = request.POST["contact_subject"]
		contact_message = request.POST["contact_message"]
		
		contactform = ContactForm(
			
			contact_name=contact_name,
			contact_email=contact_email,
			contact_subject=contact_subject,
			contact_message=contact_message,
			)

		contactform.save()
		return redirect('home')
	else:
		print("Invalid method")
		return redirect('home')	
