from rest_framework import serializers

#from .models import Produit,Vehicule,Chauffeur,Attraction,Evenement,Hopital,Bibliotheque,CentreInformation,CentreSocial
from .models import *
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produit
        fields=('name','content','prix','get_discount')

#class vehicule serializer
class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicule
        fields='__all__'

#class Chauffeur
class ChauffeurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chauffeur
        fields='__all__'


#class Attraction
class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attraction
        fields='__all__'
#class Evenement
class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Evenement
        fields='__all__'
#class Hopital
class HopitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hopital
        fields='__all__'
#class  bibliotheque

class BibliothequeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bibliotheque
        fields='__all__'
#class Centre Social
class CentreSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model=CentreSocial
        fields='__all__'

#class Centre d'information
class CentreInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CentreInformation
        fields='__all__'
#classe catégorie de evenement
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categorie
        fields='__all__'
#classe horaire de commerce
class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model=Horaire
        fields='__all__'

#classe commerce locaux

class CommerceLocauxSerailizer(serializers.ModelSerializer):
    class Meta:
        model=CommerceLocaux
        ields='__all__'




