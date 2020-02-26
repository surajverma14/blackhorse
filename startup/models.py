from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class Entity(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null ='True',blank='True')
	startup_entity_name = models.CharField(max_length=150)
	startup_logo = models.ImageField( upload_to='startup_uploads_logo')
	startup_contact_number = models.CharField(max_length=10)
	startup_bio = models.TextField()
	startup_disruption = models.TextField()
	startup_website =	models.URLField()
	startup_brand_name = models.TextField()
	startup_industry =	models.TextField()
	startup_advisors =  models.TextField()
	startup_linkedin =  models.URLField()
	startup_location = models.TextField()
	startup_funding_need = models.TextField()
	startup_business_model = models.TextField()
	startup_fund_utilize_time = models.TextField()
	startup_stage = models.TextField()
	

	def __str__(self):
		return self.startup_brand_name



class Founder(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	#entity = models.ForeignKey(Entity,on_delete=models.CASCADE)
	founder_first_name = models.CharField(max_length=150)
	founder_last_name =	 models.CharField(max_length=150)
	founder_prior =	models.TextField()
	founder_linkedin = models.URLField()
	founder_instagram = models.URLField()
	founder_contact_number = models.CharField(max_length=10)
	founder_equity = models.IntegerField()
	founder_education = models.TextField()
	founder_achievements = models.TextField()


	def __str__(self):
		return self.user



class Cofounder(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	#entity = models.OneToOneField(Entity,on_delete=models.CASCADE)
	cofounder_first_name = models.CharField(max_length=150)
	cofounder_last_name = models.CharField(max_length=10)
	cofounder_prior = models.TextField()
	cofounder_linkedin = models.URLField()
	cofounder_instagram = models.URLField()
	cofounder_contact_number = models.IntegerField()
	cofounder_equity = models.IntegerField()
	cofounder_education = models.TextField()
	cofounder_achievements = models.TextField()

	def __str__(self):
		return self.user


class Cofounder3(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	#entity = models.OneToOneField(Entity,on_delete=models.CASCADE)
	cofounder3_first_name = models.CharField(max_length=150)
	cofounder3_last_name = models.CharField(max_length=10)
	cofounder3_prior = models.TextField()
	cofounder3_linkedin = models.URLField()
	cofounder3_instagram = models.URLField()
	cofounder3_contact_number = models.IntegerField()
	cofounder3_equity = models.IntegerField()
	cofounder3_education = models.TextField()
	cofounder3_achievements = models.TextField()

	def __str__(self):
		return self.user




class Cofounder4(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	#entity = models.OneToOneField(Entity,on_delete=models.CASCADE)
	cofounder3_first_name = models.CharField(max_length=150)
	cofounder3_last_name = models.CharField(max_length=10)
	cofounder3_prior = models.TextField()
	cofounder3_linkedin = models.URLField()
	cofounder3_instagram = models.URLField()
	cofounder3_contact_number = models.IntegerField()
	cofounder3_equity = models.IntegerField()
	cofounder3_education = models.TextField()
	cofounder3_achievements = models.TextField()

	def __str__(self):
		return self.user




class Upload_video_pitch(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	#entity = models.OneToOneField(Entity,on_delete=models.CASCADE)
	upload_video_pitch = models.FileField(upload_to='startup_uploads_pitch',blank='True')

	def __str__(self):
		return self.user
	



class Upload_pitch_deck(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	upload_pitch_deck = models.FileField(upload_to='startup_uploads_deck',blank='True')
	
	def __str__(self):
		return self.user
	


class Upload_financials(models.Model):
	user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	upload_financials = models.FileField(upload_to='startup_uploads_financials',blank='True')
	
	def __str__(self):
		return self.user
		
				
class Startup_Funding_Details(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	startup_location = models.TextField()
	startup_funding_need = models.TextField()
	startup_business_model = models.TextField()
	startup_fund_utilize_time = models.TextField()
	startup_stage = models.TextField()
			
				

