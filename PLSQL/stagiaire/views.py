from django.http import HttpResponse
from django.shortcuts import render, reverse

from stage.models import Stage
from stagiaire.models import ContactForm, Stagiaire

def retourinscription(request , inscrit):
    stagiaire = Stagiaire.objects.all()
    try:
        lien = Stage.objects.get(typestage=inscrit)
    except Stage.DoesNotExist:
        # Gérer le cas où le lien n'existe pas
        return HttpResponse("Erreur")
    return render(request, 'inscription/inscription.html', {'lien': lien, 'stagiaire': stagiaire})

def retourdebut(request):
    stage = Stage.objects.all()
    return render(request, 'inscription/gestionstage.html',{'stage': stage})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponse("Well Done") # Enregistre les données du formulaire dans la base de données
    else:
        form = ContactForm()
    return render(request, 'stagiaire/stagiaire.html', {'form': form})
