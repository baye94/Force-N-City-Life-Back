
from django.shortcuts import render

from .serializers import *
from rest_framework import mixins,generics



# Create your views here.
from .models import Produit
from rest_framework.response import Response
from rest_framework.decorators import api_view

"""@api_view(['GET'])
#def api_views(request):
    #request
    #query=Produit.objects.all().order_by('?').first()
    #data={  }
 #   serializer=ProduitSerializer(data=request.data)

 #   if serializer.is_valid(raise_exception=True):
 #    serializer.save()

 #    return Response(serializer.data)
  #  else:
 #      return Response({'detail':'invalid data'}) """
"""Class pour produit"""
class  ProduitListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
       queryset = Produit.objects.all()
       serializer_class = ProduitSerializer

       def get(self, request, *args, **kwargs):
           return self.list(request, *args, **kwargs)

       def post(self, request, *args, **kwargs):
           return self.create(request, *args, **kwargs)


class ProduitRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
       queryset = Produit.objects.all()
       serializer_class = ProduitSerializer

       def get(self, request, *args, **kwargs):
           return self.retrieve(request, *args, **kwargs)

       def put(self, request, *args, **kwargs):
           return self.update(request, *args, **kwargs)

       def delete(self, request, *args, **kwargs):
           return self.destroy(request, *args, **kwargs)
       
""" class pour horaire"""
class HoraireListCreateAPIView(generics.ListCreateAPIView):
       queryset = Horaire.objects.all()
       serializer_class = HoraireSerializer
    
class HoraireRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Horaire.objects.all()
       serializer_class = HoraireSerializer

"""class  pour commerceLocaux"""

class CommerceLocauxListCreateAPIView(generics.ListCreateAPIView):
       queryset = CommerceLocaux.objects.all()
       serializer_class = CommerceLocauxSerailizer

class CommerceLocauxRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = CommerceLocaux.objects.all()
       serializer_class = CommerceLocauxSerailizer     

"""Class pour VEHICULE"""

class VehiculeListCreateAPIView(generics.ListCreateAPIView):
       queryset = Vehicule.objects.all()
       serializer_class = VehiculeSerializer

class VehiculeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Vehicule.objects.all()
       serializer_class = VehiculeSerializer

""" CLASS POUR CHAUFFEUR"""
class ChauffeurListCreateAPIView(generics.ListCreateAPIView):
       queryset = Chauffeur.objects.all()
       serializer_class = ChauffeurSerializer

class ChauffeurRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Chauffeur.objects.all()
       serializer_class = ChauffeurSerializer

""" Class pour Attraction"""
class AttractionListCreateAPIView(generics.ListCreateAPIView):
       queryset = Attraction.objects.all()
       serializer_class = AttractionSerializer

class AttractionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer



""" class pour categorie"""
class CategorieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
""" Class pour EVENEMENT"""

class EvenementListCreateAPIView(generics.ListCreateAPIView):
       queryset = Evenement.objects.all()
       serializer_class = EvenementSerializer

class EvenementRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Evenement.objects.all()
       serializer_class = EvenementSerializer

"""CLASS HOPITAL"""

class HopitalListCreateAPIView(generics.ListCreateAPIView):
       queryset = Hopital.objects.all()
       serializer_class = HopitalSerializer

class HopitalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Hopital.objects.all()
       serializer_class = HopitalSerializer
    
"""class Bibliotheque"""

class BibliothequeListCreateAPIView(generics.ListCreateAPIView):
       queryset = Bibliotheque.objects.all()
       serializer_class = BibliothequeSerializer

class BibliothequeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Bibliotheque.objects.all()
       serializer_class = BibliothequeSerializer

""" Class pour centreSocial"""
class CentreSocialListCreateAPIView(generics.ListCreateAPIView):
       queryset = CentreSocial.objects.all()
       serializer_class = CentreSocialSerializer

class CentreSocialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = CentreSocial.objects.all()
       serializer_class = CentreSocialSerializer

""" Class pour CentreInformation"""

class CentreInformationListCreateAPIView(generics.ListCreateAPIView):
       queryset = CentreInformation.objects.all()
       serializer_class = CentreInformationSerializer

class CentreInformationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
       queryset = CentreInformation.objects.all()
       serializer_class = CentreInformationSerializer