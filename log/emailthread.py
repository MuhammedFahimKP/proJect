
from threading  import Thread
from .models import MyUser
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage


class EmailThread(Thread):

    def __init__(self,req,email,user):
        self.email=email   
        self.req = req
        self.user = user 
        Thread.__init__(self)


    def run(self):
            current_site = get_current_site(self.req)
            mail_subject = 'Activate Your Account'
            message      = render_to_string('log/activation.html',{
                'user':self.user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(self.user.id)),
                'token':default_token_generator.make_token(self.user),
            })

            to_email = self.email
            sendemail = EmailMessage(mail_subject,message,to=[to_email]) 
            sendemail.send()    

         


