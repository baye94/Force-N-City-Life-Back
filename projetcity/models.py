from django.db import models

# Create your models here.
class Produit(models.Model):
    prix=models.DecimalField(max_digits=15, decimal_places=2)
    name=models.CharField(max_length=20)
    content=models.TextField()
    @property
    def get_discount(self):
        return "%.2f"%(float(self.prix)*0.5)
#classe horaire
class Horaire(models.Model):
    jour = models.CharField(max_length=20)
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()
    
#COMMERCE LOCAUX
class CommerceLocaux(models.Model):
    nom = models.CharField(max_length=100)
    Produits=models.produits = models.ManyToManyField(Produit)
    horaire = models.OneToOneField(Horaire, on_delete=models.CASCADE)


#classe vehicule
class Vehicule(models.Model):
       #marque = models.CharField(max_length=50)
    TYPE={'train':'train',
          'bus':'bus', 
          'metro':'metro'
          }
    modele = models.CharField(max_length=50)
    type=models.CharField(max_length=100,choices=TYPE)
    tarif = models.DecimalField(max_digits=10, decimal_places=2)
    itinéraire=models.CharField(max_length=100)
       #annee_fabrication = models.PositiveIntegerField()
       #couleur = models.CharField(max_length=30)
       #plaque_immatriculation = models.CharField(max_length=15, unique=True)
#model chauffeur
class Chauffeur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
#Attraction
class Attraction(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_ouverture = models.DateField()
    capacite_maximale = models.PositiveIntegerField()
    tarif = models.DecimalField(max_digits=10, decimal_places=2)
#classe categorie
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
#classe évenement
class Evenement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    categorie = models.OneToOneField(Categorie, on_delete=models.CASCADE)
 #hopital
class Hopital(models. Model) :
    nom = models. CharField(max_length=100)
    adresse = models.TextField()
    téléphone = models.CharField(max_length=20)
    capacite_lits = models.IntegerField()
#class bibliothéque
class Bibliotheque(models.Model):
    nom = models. CharField(max_length=100)
    adresse = models.TextField()
    téléphone = models.CharField(max_length=20)
#class centre social
class CentreSocial(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    capacite_accueil = models.PositiveIntegerField()
#class centre d'information
    
class CentreInformation(models.Model):
       nom = models.CharField(max_length=100)
       adresse = models.TextField()
       telephone = models.CharField(max_length=20)
       responsable = models.CharField(max_length=100)



