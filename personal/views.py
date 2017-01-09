from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'personal/home.html')
	
def contact(request):
	return render(request, 'personal/basic.html', {'content':['About me. I am a 19 year old girl, studying Psychology and Technology. I have chosen to follow some electives in ICT, Webtechnology is the first of these. Therefore, it is sometimes quite a struggle to keep up with everything. But I will manage :D'  ]})
	

		
