from django.shortcuts import render
from django.http import HttpResponse
# from django.core.mail import EmailMessage, get_connection
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def send_email(request):  
#    if request.method == "POST": 
#        with get_connection(  
#            host=settings.EMAIL_HOST, 
#      port=settings.EMAIL_PORT,  
#      username=settings.EMAIL_HOST_USER, 
#      password=settings.EMAIL_HOST_PASSWORD, 
#      use_tls=settings.EMAIL_USE_TLS  
#        ) as connection:  
#            subject = request.POST.get("subject")  
#            email_from = settings.EMAIL_HOST_USER  
#            recipient_list = [request.POST.get("email"), ]  
#            message = request.POST.get("message")  
#            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
 
#    return render(request, 'file.html')

from django.core.mail import send_mail

def send_emails(request):
    subject = 'Detailed explanation of concerned issue'
    message = 'Thank you for reaching out to us. We are happy to help and listen to you. Please visit the link and provide a detailed overview of you concern. USERNAME:emailid, PASSWORD:referral id'
    from_email = 'krangarius@gmail.com'
    recipient_list = ['9415kks@gmail.com']

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Emails sent successfully")

# Create your views here.
