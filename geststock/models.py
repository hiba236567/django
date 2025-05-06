from django.db import models

class Product(models.Model):
    nom_produit = models.CharField(max_length=100)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_entree = models.DateField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_produit 