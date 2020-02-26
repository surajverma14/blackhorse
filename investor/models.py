from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class InvestorDetail(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null ='True',blank='True')
	investor_entity_name = models.CharField(max_length=150)
	investor_logo = models.ImageField(default='/img/HRS.PNG', upload_to='investor_uploads_logo')
	investor_contact_number = models.CharField(max_length=10)
	investor_email =	models.EmailField(max_length=254)
	investor_linkedin =  models.URLField()
	investor_full_name = models.CharField(max_length=250)
	
	

	def __str__(self):
		return self.investor_entity_name




class InvestorThesis(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null ='True',blank='True')
	#investor_detail = models.ForeignKey(InvestorDetail,on_delete=models.CASCADE)
	investor_stage = models.CharField(max_length=150)
	investor_ticket_size = models.TextField(max_length=150)
	investor_return_expectx = models.CharField(max_length=150)
	# investor_return_expectp = models.CharField(max_length=150)
	investor_exit_time = models.CharField(max_length=150)
	investor_industry =	models.TextField()
	investor_geography = models.CharField(max_length=150)
	investor_business_model = models.TextField()

