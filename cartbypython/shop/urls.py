from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<param>/", views.product, name="product"),
    path("panier", views.cart, name="panier"),
    path("panier-produit/<param>/", views.cartProduct, name="panier_produit"),
    path("panier-produit-modifier-quantite", views.cartUpdateQuantityProduct, name="panier_produit_modifier_quantite"),
    path("panier-supprimer-produit/<param>/", views.removeProduct, name="panier_supprimer_produit"),
]
