from django.shortcuts import render, HttpResponseRedirect, redirect
from django.forms import ModelForm
from .models import Contact
from django.urls import reverse, reverse_lazy
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib import messages

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            titre = f'Cuisine Antillaise | {firstname} {lastname} - {email}'
            send_mail(titre, message, 'david.accipe@gmail.com', ['contact@informatikmarket.com'])

            
        return HttpResponseRedirect(reverse('informations:remerciements'))
    return render(request, 'informations/contact.html', {'form': form})

def remerciements_view(request):
    return render(request, 'informations/remerciements.html')
    # return HttpResponse('Merci de nous avoir contacté')



def mode_livraison(request):
    return render(request, 'informations/modelivraison.html')


def mode_paiement(request):
    return render(request, 'informations/modepaiement.html')


def paiement_securise(request):
    return render(request, 'informations/paiementsecurise.html')


def politique_confidentialite(request):
    return render(request, 'informations/politiqueconfidentialite.html')


def politique_remboursement(request):
    return render(request, 'informations/politiqueremboursement.html')


def politique_kookies(request):
    return render(request, 'informations/politiquekookies.html')


def condition_generale(request):
    return render(request, 'informations/conditiongenerale.html')

