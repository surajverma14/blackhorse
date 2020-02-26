from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import InvestorDetail ,InvestorThesis
from django.contrib.auth.models import User
from core.models import UserProfile
from django.views.generic import ListView ,DetailView
from startup.models import Entity

 #	Create your views here.


def investor(request):
	context = {
	'InvestorDetail' : InvestorDetail.objects.all(),
	'InvestorThesis' : InvestorThesis.objects.all()
	
	 }
	if request.user.is_authenticated:
		user = UserProfile.objects.get(user_id=request.user.id).label
		if user: 
			return render(request,'investor/investor.html', context)
		else:
			return render(request,'accounts/login.html') #and user_type.objects.get(user=request.user).is_investor: 
	else:
		return redirect('login')	



# def iopportunity(request):
# 			return render(request,'investor/opportunities.html')		


def investor_own_profile(request):
	if request.user.is_authenticated:


		return render(request,'investor/idetail.html') 

	else:
		return redirect('login')	





class StartupListView(ListView):
	queryset = Entity.objects.all()
	model = Entity
	template_name = 'investor/opportunities.html'
	context_object_name = 'entity' 


# class InvestorDetailView(DetailView):

# 	queryset = InvestorDetail.objects.all()

# 	template_name = 'investor/investor-detail-view.html'
# 	model = InvestorDetail
# 	context = 'investordetail'
# 	def get_context_data(self, **kwargs):

# 		context = super(InvestorDetailView, self).get_context_data(**kwargs)
# 		context['investorthesis'] =InvestorThesis.objects.all()
# 		# And so on for more models
# 		return context
def Investordetails(request,pk):
	
	# entity = get_object_or_404(Entity, user_id=request.user.id)
	investordetail= InvestorDetail.objects.filter(user_id=pk)
	investorthesis=InvestorThesis.objects.filter(user_id=pk)

	context = {

	'investordetail' : investordetail[0],
	'investorthesis': investorthesis[0],
	 } 
	
	return render(request,'investor/investor-detail-view.html', context)



def investor_detail_submission(request):
	if request.method =='POST':
		value=InvestorDetail.objects.filter(user_id=request.user.id)
		if value[0]:

			InvestorDetail.objects.filter(user_id=request.user.id).update(investor_logo=request.FILES["investor_logo"],
			investor_full_name=request.POST["investor_full_name"],investor_contact_number = request.POST["investor_contact_number"],
			investor_email = request.POST["investor_email"],investor_linkedin = request.POST["investor_linkedin"],
			investor_entity_name= request.POST["investor_entity_name"])
			# investordetail =InvestorDetail()
				
			# if request.FILES["investor_logo"]:
			# 	investordetail.investor_logo = request.FILES["investor_logo"]
			# if request.POST["investor_full_name"]:
			# 	investordetail.investor_full_name = request.POST["investor_full_name"]
			# if request.POST["investor_contact_number"]:
			# 	investordetail.investor_contact_number = request.POST["investor_contact_number"]
			# if request.POST["investor_email"]:	
			# 	investordetail.investor_email = request.POST["investor_email"]
			# if request.POST["investor_linkedin"]:	
			# 	investordetail.investor_linkedin = request.POST["investor_linkedin"]
			# if request.POST["investor_entity_name"]:
			# 	investordetail.investor_entity_name = request.POST["investor_entity_name"]
			
			# investordetail.save()
			return redirect('investor')

		else:
			

			user = request.user
			investor_logo = request.FILES["investor_logo"]
			investor_full_name = request.POST["investor_full_name"]
			investor_contact_number = request.POST["investor_contact_number"]
			investor_email = request.POST["investor_email"]
			investor_linkedin = request.POST["investor_linkedin"]
			investor_entity_name = request.POST["investor_entity_name"]


			investordetail = InvestorDetail(
				user=user,
				investor_logo=investor_logo,
				investor_full_name=investor_full_name,
				investor_contact_number=investor_contact_number,
				investor_email=investor_email,
				investor_linkedin=investor_linkedin,
				investor_entity_name=investor_entity_name)
				
				
			investordetail.save()
			return redirect('investor')
	else:
		print("Invalid method")
		return redirect('investor')	



def investor_thesis_submission(request):
	if request.method =='POST':
		value=InvestorThesis.objects.filter(user_id=request.user.id)
		if value[0]:
			# print( request.POST)
			# print( request.POST.getlist('investor_stage'))
			# return redirect('investor')
			InvestorThesis.objects.filter(user_id=request.user.id).update(investor_stage = request.POST['investor_stage'],
			investor_ticket_size = request.POST["investor_ticket_size"],investor_return_expectx = request.POST["investor_return_expectx"],
			investor_exit_time = request.POST["investor_exit_time"],investor_industry = request.POST["investor_industry"],
			investor_geography = request.POST["investor_geography"],investor_business_model = request.POST["investor_business_model"])
			return redirect('investor')
		else:
			user = request.user
			investor_stage = request.POST['investor_stage']
			investor_ticket_size = request.POST["investor_ticket_size"]
			investor_return_expectx = request.POST["investor_return_expectx"]
			# investor_return_expectp = request.POST["investor_return_expectp"]
			investor_exit_time = request.POST["investor_exit_time"]
			investor_industry = request.POST["investor_industry"]
			investor_geography = request.POST["investor_geography"]
			investor_business_model = request.POST["investor_business_model"]
			investorthesis = InvestorThesis(
				user=user,
				investor_stage=investor_stage,
				investor_ticket_size=investor_ticket_size,
				investor_return_expectx=investor_return_expectx,
				# investor_return_expectp=investor_return_expectp,
				investor_exit_time=investor_exit_time,
				investor_industry=investor_industry,
				investor_geography=investor_geography,
				investor_business_model=investor_business_model,
				)

			investorthesis.save()
			return redirect('investor')
	else:
		print("Invalid method")
		return redirect('investor')	


