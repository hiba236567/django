from django.shortcuts import render, redirect
from django import forms
from .models import Product

class StockForm(forms.Form):
    nom_produit = forms.CharField(label='Nom du Produit', max_length=100)
    quantite = forms.IntegerField(label='Quantité')
    prix_unitaire = forms.DecimalField(label='Prix Unitaire', max_digits=10, decimal_places=2)
    date_entree = forms.DateField(label='Date d\'entrée', widget=forms.DateInput(attrs={'type': 'date'}))

def index(request):
    return render(request, 'index.html')

def form_view(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            # Sauvegarder le produit dans la base de données
            Product.objects.create(
                nom_produit=form.cleaned_data['nom_produit'],
                quantite=form.cleaned_data['quantite'],
                prix_unitaire=form.cleaned_data['prix_unitaire'],
                date_entree=form.cleaned_data['date_entree']
            )
            return redirect('trait')  # Redirige vers la page de traitement après l'enregistrement
    else:
        form = StockForm()
    
    return render(request, 'form.html', {'form': form})

def trait_view(request):
    # Récupérer tous les produits de la base de données
    produits = Product.objects.all().order_by('-date_creation')
    return render(request, 'trait.html', {'produits': produits})
