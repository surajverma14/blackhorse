from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import Entity , Founder ,Cofounder , Upload_video_pitch,Startup_Funding_Details, Upload_pitch_deck, Upload_financials , Cofounder3 ,Cofounder4
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from core.models import UserProfile 
from investor.views import InvestorThesis , InvestorDetail
from django.views.generic import ListView ,DetailView,TemplateView
from django.shortcuts import get_object_or_404




 #	Create your views here. 


def startup(request):
	context = {
	'entity' : Entity.objects.all(),
	'founder': Founder.objects.all(),
	'cofounder': Cofounder.objects.all(),
	'cofounder3' : Cofounder3.objects.all(),
	'cofounder4' : Cofounder4.objects.all(),
	'upload_video_pitch' : Upload_video_pitch.objects.all(),
	'upload_pitch_deck' : Upload_pitch_deck.objects.all(),
	'upload_financials' : Upload_financials.objects.all(),
	'title' : 'Startup'
	 } 
	if request.user.is_authenticated:
		user = UserProfile.objects.get(user_id=request.user.id).label
		if user=='S': 
			return render(request,'startup/startup.html', context)
		elif user=='I':
			return redirect('investor')	
	else:
		return render(request,'accounts/login.html')	



def plans(request):
	if request.user.is_authenticated: #and user_type.objects.get(user=request.user).is_startup:
		return render(request,'startup/plans.html',{'title' : 'Plans'})
	else:
		return render(request,'accounts/login.html')


def startup_own_profile(request):
	if request.user.is_authenticated:
		user = UserProfile.objects.get(user_id=request.user.id).label
		if user=='S': 
			return render(request,'startup/sprofile.html')
		else:
			return render(request,'accounts/login.html')
	else:
		return render(request,'accounts/login.html')






# class StartupDetailView(DetailView):
# 	queryset = Entity.objects.all()
# 	# queryset=Founder.objects.all()
# 	model = Entity
# 	template_name = 'startup/startup_detail_view.html'
# 	context_object_name = 'entity'
# class StartupDetailView(TemplateView):

#     template_name = 'startup/startup_detail_view.html'

#     def get_context_data(self, **kwargs):
#         context = super(StartupDetailView, self).get_context_data(**kwargs)
#         context['entity'] = Entity.objects.all()
#         return context

def startupdetails(request,pk):
	
	# entity = get_object_or_404(Entity, user_id=request.user.id)
	entity=Entity.objects.filter(user_id=pk)
	founder= Founder.objects.filter(user_id=pk)
	# cofounder= Cofounder.objects.filter(user_id=pk)
	# cofounder3= Cofounder3.objects.filter(user_id=pk)
	# cofounder4=Cofounder4.objects.filter(user_id=pk)
	upload_video_pitch=Upload_video_pitch.objects.filter(user_id=pk)
	upload_pitch_deck=Upload_pitch_deck.objects.filter(user_id=pk)
	upload_financials= Upload_financials.objects.filter(user_id=pk)
	if upload_financials:
		financial=upload_financials[0]
	else:
		financial=upload_financials

	if upload_pitch_deck:
		deck=upload_pitch_deck[0]
	else:
		deck=upload_pitch_deck

	if upload_video_pitch:
		video=upload_video_pitch[0]
	else:
		video=upload_video_pitch
	context = {

	'entity' : entity[0],
	'founder':founder[0],
	'upload_video_pitch' :video,
	'upload_pitch_deck' : deck,
	'upload_financials' :financial,
	'title' : 'Startup'
	 } 
	
	return render(request,'startup/startup_detail_view.html', context)

# def sopportunity(request): 
# 	return render(request,'startup/opportunity.html')


class InvestorListView(ListView):
	queryset = InvestorThesis.objects.all()
	
	#model = Entity
	template_name = 'startup/opportunity.html'
	context_object_name = 'investorthesis'



def startup_entity_submission(request):
	

	if request.method =='POST':
		#uploaded_file = request.FILES['document']
		#print(uploaded_file.name)
		#print(uploaded_file.size)
		#fs=FileSystemStorage()
		#fs.save(startup_logo.name,startup_logo)
		value=Entity.objects.filter(user_id=request.user.id)
		if value[0]:
			Entity.objects.filter(user_id=request.user.id).update(startup_logo = request.FILES["logo"],startup_entity_name = request.POST["startup_entity_name"],
			startup_contact_number = request.POST["startup_contact_number"],startup_bio = request.POST["startup_bio"],startup_disruption = request.POST["startup_disruption"],
			startup_website = request.POST["startup_website"],startup_brand_name = request.POST["startup_brand_name"],startup_industry = request.POST["startup_industry"],
			startup_advisors = request.POST["startup_advisors"],
			startup_linkedin = request.POST["startup_linkedin"],
			startup_location = request.POST["startup_location"],
			startup_stage = request.POST["startup_stage"],
			startup_business_model = request.POST["startup_business_model"],
			startup_funding_need = request.POST["startup_funding_need"])
			return redirect('startup')
		else:	
			user = request.user
			startup_logo = request.FILES["logo"]
			startup_entity_name = request.POST["startup_entity_name"]
			startup_contact_number = request.POST["startup_contact_number"]
			startup_bio = request.POST["startup_bio"]
			startup_disruption = request.POST["startup_disruption"]
			startup_website = request.POST["startup_website"]
			startup_brand_name = request.POST["startup_brand_name"]
			startup_industry = request.POST["startup_industry"]
			startup_advisors = request.POST["startup_advisors"]
			startup_linkedin = request.POST["startup_linkedin"]
			startup_location = request.POST["startup_location"]
			startup_stage = request.POST["startup_stage"]
			startup_business_model = request.POST["startup_business_model"]
			startup_funding_need = request.POST["startup_funding_need"]
			

			entity = Entity(
				user=user,
				startup_logo=startup_logo,
				startup_linkedin=startup_linkedin,
				startup_advisors=startup_advisors,
				startup_industry=startup_industry,
				startup_brand_name=startup_brand_name,
				startup_website=startup_website,
				startup_disruption=startup_disruption,
				startup_bio=startup_bio,
				startup_entity_name=startup_entity_name,
				startup_contact_number=startup_contact_number,
				startup_location=startup_location,
				startup_stage=startup_stage,
				startup_business_model=startup_business_model,
				startup_funding_need=startup_funding_need
				)

			entity.save()
			return redirect('startup')
	else:
		print("Invalid method")
		return redirect('startup')	


def startup_founder_submission(request):
	if request.method =='POST':
		value=Founder.objects.filter(user_id=request.user.id)
		if value[0]:
			Founder.objects.filter(user_id=request.user.id).update(founder_first_name = request.POST["founder_first_name"],
			founder_last_name = request.POST["founder_last_name"],
			founder_prior = request.POST["founder_prior"],
			founder_linkedin = request.POST["founder_linkedin"],
			founder_instagram= request.POST["founder_instagram"],
			founder_contact_number = request.POST["founder_contact_number"],
			founder_equity = request.POST["founder_equity"],
			founder_education = request.POST["founder_education"],
			founder_achievements = request.POST["founder_achievements"])
			return redirect('startup')
		else:	
			user = request.user
			founder_first_name = request.POST["founder_first_name"]
			founder_last_name = request.POST["founder_last_name"]
			founder_prior = request.POST["founder_prior"]
			founder_linkedin = request.POST["founder_linkedin"]
			founder_instagram= request.POST["founder_instagram"]
			founder_contact_number = request.POST["founder_contact_number"]
			founder_equity = request.POST["founder_equity"]
			founder_education = request.POST["founder_education"]
			founder_achievements = request.POST["founder_achievements"]

			founder = Founder(
			user=user,
			founder_first_name=founder_first_name,
			founder_last_name=founder_last_name,
			founder_prior=founder_prior,
			founder_linkedin=founder_linkedin,
			founder_instagram=founder_instagram,
			founder_contact_number=founder_contact_number,
			founder_equity=founder_equity,
			founder_education=founder_education,
			founder_achievements=founder_achievements)
			founder.save()
			return redirect('startup')

	else:
		print("Invalid method")
		return redirect('startup')




def startup_cofounder_submission(request):
	if request.method =='POST':	
		value=Cofounder.objects.filter(user_id=request.user.id)
		if value[0]:
			Cofounder.objects.filter(user_id=request.user.id).update(cofounder_first_name = request.POST["cofounder_first_name"],
			cofounder_last_name = request.POST["cofounder_last_name"],
			cofounder_prior = request.POST["cofounder_prior"],
			cofounder_linkedin = request.POST["cofounder_linkedin"],
			cofounder_instagram = request.POST["cofounder_instagramv"],
			cofounder_contact_number = request.POST["cofounder_contact_number"],
			cofounder_equity = request.POST["cofounder_equity"],
			cofounder_education = request.POST["cofounder_education"],
			cofounder_achievements = request.POST["cofounder_achievements"])
			return redirect('startup')
		else:	
			user = request.user
			cofounder_first_name = request.POST["cofounder_first_name"]
			cofounder_last_name = request.POST["cofounder_last_name"]
			cofounder_prior = request.POST["cofounder_prior"]
			cofounder_linkedin = request.POST["cofounder_linkedin"]
			cofounder_instagram = request.POST["cofounder_instagramv"]
			cofounder_contact_number = request.POST["cofounder_contact_number"]
			cofounder_equity = request.POST["cofounder_equity"]
			cofounder_education = request.POST["cofounder_education"]
			cofounder_achievements = request.POST["cofounder_achievements"]

			cofounder=Cofounder(user=user,
			cofounder_first_name=cofounder_first_name,
			cofounder_last_name=cofounder_last_name,
			cofounder_prior=cofounder_prior,
			cofounder_linkedin=cofounder_linkedin,
			cofounder_instagram=cofounder_instagram,
			cofounder_contact_number=cofounder_contact_number,
			cofounder_equity=cofounder_equity,
			cofounder_education=cofounder_education,
			cofounder_achievements=cofounder_achievements)
			cofounder.save()
			return redirect('startup')

	else:
		print("Invalid method")
		return redirect('startup')



def startup_cofounder4_submission(request):
	if request.method =='POST':	
		user = request.user
		cofounder4_first_name = request.POST["cofounder4_first_name"]
		cofounder4_last_name = request.POST["cofounder4_last_name"]
		cofounder4_prior = request.POST["cofounder4_prior"]
		cofounder4_linkedin = request.POST["cofounder4_linkedin"]
		cofounder4_instagram = request.POST["cofounder4_instagramv"]
		cofounder4_contact_number = request.POST["cofounder4_contact_number"]
		cofounder4_equity = request.POST["cofounder4_equity"]
		cofounder4_education = request.POST["cofounder4_education"]
		cofounder4_achievements = request.POST["cofounder4_achievements"]

		cofounder4=Cofounder(user=user,
		cofounder4_first_name=cofounder_first_name,
		cofounder4_last_name=cofounder4_last_name,
		cofounder4_prior=cofounder4_prior,
		cofounder4_linkedin=cofounder4_linkedin,
		cofounder4_instagram=cofounder4_instagram,
		cofounder4_contact_number=cofounder4_contact_number,
		cofounder4_equity=cofounder4_equity,
		cofounder4_education=cofounder4_education,
		cofounder4_achievements=cofounder4_achievements)
		cofounder4.save()
		return redirect('startup')

	else:
		print("Invalid method")
		return redirect('startup')		


def startup_cofounder3_submission(request):
	if request.method =='POST':	
		user = request.user
		cofounder3_first_name = request.POST["cofounder3_first_name"]
		cofounder3_last_name = request.POST["cofounder3_last_name"]
		cofounder3_prior = request.POST["cofounder3_prior"]
		cofounder3_linkedin = request.POST["cofounder3_linkedin"]
		cofounder3_instagram = request.POST["cofounder3_instagramv"]
		cofounder3_contact_number = request.POST["cofounder3_contact_number"]
		cofounder3_equity = request.POST["cofounder3_equity"]
		cofounder3_education = request.POST["cofounder3_education"]
		cofounder3_achievements = request.POST["cofounder3_achievements"]

		cofounder3=Cofounder3(user=user,
		cofounder3_first_name=cofounder3_first_name,
		cofounder3_last_name=cofounder3_last_name,
		cofounder3_prior=cofounder3_prior,
		cofounder3_linkedin=cofounder3_linkedin,
		cofounder3_instagram=cofounder3_instagram,
		cofounder3_contact_number=cofounder3_contact_number,
		cofounder3_equity=cofounder3_equity,
		cofounder3_education=cofounder3_education,
		cofounder3_achievements=cofounder3_achievements)
		cofounder3.save()
		return redirect('startup')

	else:
		print("Invalid method")
		return redirect('startup')




def startup_funding_submission(request):
	if request.method =='POST':
		value=Startup_Funding_Details.objects.filter(user_id=request.user.id)
		if value[0]:
			Startup_Funding_Details.objects.filter(user_id=request.user.id).update(startup_location = request.POST["startup_location"],
			startup_stage = request.POST["startup_stage"],
			startup_business_model = request.POST["startup_business_model"],
			startup_funding_need = request.POST["startup_funding_need"],
			)	
			return redirect('startup')
		else:
			user = request.user
			startup_location = request.POST["startup_location"]
			startup_stage = request.POST["startup_stage"]
			startup_business_model = request.POST["startup_business_model"]
			startup_funding_need = request.POST["startup_funding_need"]
			

			startup_funding_details=Startup_Funding_Details(user=user,
			startup_location=startup_location,
			startup_stage=startup_stage,
			startup_business_model=startup_business_model,
			startup_funding_need=startup_funding_need)

			startup_funding_details.save()
			return redirect('startup')

	else:
		print("Invalid method")
		return redirect('startup')







def startup_video_submission(request):	
	if request.method =='POST':
		value=Upload_video_pitch.objects.filter(user_id=request.user.id)
		if value[0]:
			Upload_video_pitch.objects.filter(user_id=request.user.id).update(upload_video_pitch = request.FILES["video"])	
			return redirect('startup')
		else:
			user = request.user
			upload_video_pitch = request.FILES["video"]
			#upload_pitch_deck = request.FILES["deck"]
			#upload_financials = request.FILES["finan"]
			#fs=FileSystemStorage()
			#gs=FileSystemStorage()
			#hs=FileSystemStorage()
			#fs.save(upload_video_pitch.name,upload_video_pitch)
			#gs.save(upload_pitch_deck.name,uploadload_pitch_deck)
			#hs.save(upload_financials.name,upload_financials)
			
			upload_video_pitch=Upload_video_pitch(user=user,upload_video_pitch=upload_video_pitch)
			upload_video_pitch.save()
			#upload=Upload(upload_pitch_deck=upload_pitch_deck,)
			#	upload_video_pitch=upload_video_pitch,
			#	upload_financials=upload_financials)

			#upload.save()
			return redirect('startup')

	else:
		print("Invalid method")
		return redirect('startup')	


def startup_deck_submission(request):	
	if request.method =='POST':
		value=Upload_pitch_deck.objects.filter(user_id=request.user.id)
		if value[0]:
			Upload_pitch_deck.objects.filter(user_id=request.user.id).update(upload_pitch_deck = request.FILES["deck"])	
			return redirect('startup')
		else:
			user = request.user
			upload_pitch_deck = request.FILES["deck"]
			#upload_pitch_deck = request.FILES["deck"]
			#upload_financials = request.FILES["finan"]
			#hs=FileSystemStorage()
			#gs=FileSystemStorage()
			#hs=FileSystemStorage()
			#hs.save(upload_video_pitch.name,upload_video_pitch)
			#gs.save(upload_pitch_deck.name,upload_pitch_deck)
			#hs.save(upload_financials.name,upload_financials)
			upload_pitch_deck=Upload_pitch_deck(user=user,upload_pitch_deck=upload_pitch_deck)
			upload_pitch_deck.save()
			#upload=Upload(upload_pitch_deck=upload_pitch_deck,)
			#	upload_video_pitch=upload_video_pitch,
			#	upload_financials=upload_financials)

			#upload.save()
			return redirect('startup')

	else:
		print("Invalid method")
		return redirect('startup')	



def startup_finan_submission(request):	
	if request.method =='POST':
		value=Upload_financials.objects.filter(user_id=request.user.id)
		if value[0]:
			Upload_financials.objects.filter(user_id=request.user.id).update(upload_financials = request.FILES["finan"])	
			return redirect('startup')
		else:
			user = request.user
			upload_financials = request.FILES["finan"]
			#upload_pitch_deck = request.FILES["deck"]
			#upload_financials = request.FILES["finan"]
			#gs=FileSystemStorage()
			#gs=FileSystemStorage()
			#hs=FileSystemStorage()
			#gs.save(upload_video_pitch.name,upload_video_pitch)
			#gs.save(upload_pitch_deck.name,upload_pitch_deck)
			#hs.save(upload_financials.name,upload_financials)
			upload_financials=Upload_financials(user=user,upload_financials=upload_financials)
			upload_financials.save()
			#upload=Upload(upload_pitch_deck=upload_pitch_deck,)
			#	upload_video_pitch=upload_video_pitch,
			#	upload_financials=upload_financials)

			#upload.save()
			return redirect('startup')

	else:
		print("Invalid method")
		return redirect('startup')	





