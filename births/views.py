from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django import forms
from django.core.context_processors import csrf
from captcha.fields import CaptchaField
from births.models import Birth

class CaptchaContactForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(max_length=100)
    email = forms.EmailField()
    captcha = CaptchaField()

class CaptchaBirthForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Birth
        fields =('title','content','year','place','city','country','name','email')

def home(request):
    return render_to_response('index.html', {'birth_list': Birth.objects.all()}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def contact(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = CaptchaContactForm(request.POST)
        if form.is_valid():
            human = True
            subject   = form.cleaned_data['subject']
            message   = form.cleaned_data['message']
            email     = form.cleaned_data['email']
            recipients = ['contacto@partosencasa.org']

            send_mail(subject, message, email, recipients)
            return HttpResponseRedirect('/gracias/')
    else:
        form = CaptchaContactForm()

    return render_to_response('contact.html',locals(), context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html',{'mensaje': 'Recibimos tu mensaje! Gracias por Contactarnos!'}, context_instance=RequestContext(request))

def thanks_birth(request):
    return render_to_response('thanks.html',{'mensaje': 'Recibimos tu historia! Gracias por Compartirla!'}, context_instance=RequestContext(request))

def post_birth(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = CaptchaBirthForm(request.POST)
        if form.is_valid():
            human = True
            # save the data
            form.save()
            return HttpResponseRedirect('/gracias/por/tu/historia/')
    else:
        form = CaptchaBirthForm()
 
    return render_to_response('birth_form.html', locals(), context_instance=RequestContext(request))

def get_birth(request, bslug):
    birth = Birth.objects.get(slug=bslug)
    return render_to_response('birth.html', {'birth': birth}, context_instance=RequestContext(request))
