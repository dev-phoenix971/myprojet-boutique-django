from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('remerciements/', views.remerciements_view, name='remerciements'),
    path('modelivraison/', views.mode_livraison, name='modelivraison'),
    path('modepaiement/', views.mode_paiement, name='modepaiement'),
    path('paiementsecurise/', views.paiement_securise, name='paiementsecurise'),
    path('politiqueconfidentialite/', views.politique_confidentialite, name='politiqueconfidentialite'),
    path('politiqueremboursement', views.politique_remboursement, name='politiqueremboursement'),
    path('politiquekookies/', views.politique_kookies, name='politiquekookies'),
    path('conditiongenerale/', views.condition_generale, name='conditiongenerale'),

]
