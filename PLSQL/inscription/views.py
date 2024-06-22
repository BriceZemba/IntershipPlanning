from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.http import JsonResponse
from inscription.models import Inscription
from stage.models import Stage
from stagiaire.models import Stagiaire

# Create your views here.

def inscription(request, inscrit):
    stagiaire = Stagiaire.objects.all()
    try:
        lien = Stage.objects.get(typestage=inscrit)
    except Stage.DoesNotExist:
        # Gérer le cas où le lien n'existe pas
        return HttpResponse("Erreur")
    return render(request, 'inscription/inscription.html', {'lien': lien, 'stagiaire': stagiaire})


def stagiaire(request):
    return render(request, 'stagiaire/stagiaire.html')

def retour(request, retour):
    stage = Stage.objects.all()
    try:
        lien = Stage.objects.get(typestage=retour)
    except Stage.DoesNotExist:
        # Gérer le cas où le lien n'existe pas
        return HttpResponse("Erreur")
    return render(request, 'inscription/gestionstage.html', {'lien': lien, 'stage': stage})

"""def inscription_view(request):
    if request.method == 'POST':
        # Récupérer les informations du formulaire
        codestage = request.POST.get('codestage')
        numstagiaire = request.POST.get('numstagiaire')
        dateinsc = request.POST.get('dateinsc')
        statusinscr = '0'  # Définir statusinscr à 0
        codeposition = '0'  # Définir codeposition à 0

        # Créer une nouvelle instance d'Inscription et enregistrer dans la base de données
        inscription = Inscription.objects.create(codestage=codestage, numstagiaire=numstagiaire, dateinsc=dateinsc, statusinscr=statusinscr, codeposition=codeposition)
        
        # Rediriger vers une page de confirmation ou une autre page
        return render(request , 'stagiaire/stagiaire.html')  # Assurez-vous de définir une URL pour la page de confirmation dans vos urls.py
        
    else:
        # Gérer le cas où la requête n'est pas de type POST si nécessaire
        pass"""
