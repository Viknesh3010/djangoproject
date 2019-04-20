from django.shortcuts import render
import datetime  
# Create your views here.  
from django.http import HttpResponse,HttpResponseNotFound  
from django.views.decorators.http import require_http_methods 
from django.template import loader  
from djangoapp.forms import EmpForm
from django.core.mail import send_mail  
from myapp import settings   
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")
@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>') 
def login(request):  
    if request.method == "POST":  
        form = EmpForm(request.POST)  
        if form.is_valid():  
            try:  
                handle_uploaded_file(request.FILES['file'])  
                return HttpResponse("File uploaded successfuly")  
            except:  
                pass  
    else:  
         form = EmpForm()  
         return render(request,"index.html",{'form':form})
def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = "hviknesh3010@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)
	
	