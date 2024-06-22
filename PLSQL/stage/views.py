from django.http import HttpResponse
from django.shortcuts import render

from stage.models import Stage
from stagiaire.models import Stagiaire

# Create your views here.

def home(request):
    order_by = request.GET.get('order_by', '')  # Obtenir le paramètre 'order_by' de l'URL
    if order_by == 'date':
        stages = Stage.objects.all().order_by('datedebut')  # Trier par date de début
    elif order_by == 'type':
        stages = Stage.objects.all().order_by('-typestage')  # Trier par type de manière décroissante
    else:
        stages = Stage.objects.all()  # Récupérer tous les stages par défaut
    
    context = {'stage': stages}
    return render(request, 'inscription/gestionstage.html', context)

def detail_lien(request, nom_lien):
    stagiaire = Stagiaire.objects.all()
    try:
        lien = Stage.objects.get(typestage=nom_lien)
    except Stage.DoesNotExist:
        # Gérer le cas où le lien n'existe pas
        return HttpResponse("Erreur")
    return render(request, 'stage/modifstage.html', {'lien': lien , 'stagiaire':stagiaire})

"""def inscription(request):
    stagiaire = Stagiaire.objects.all()
    try:
        lien = Stage.objects.all()
    except Stage.DoesNotExist:
        # Gérer le cas où le lien n'existe pas
        return HttpResponse("Erreur")
    return render(request, 'inscription/inscription.html', {'lien': lien, 'stagiaire': stagiaire})"""

def retourdebut(request):
    stage = Stage.objects.all()
    return render(request , 'inscription/gestionstage.html' , {"stage":stage})


