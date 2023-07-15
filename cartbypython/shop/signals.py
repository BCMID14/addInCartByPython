from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os
from .models import Product

@receiver(post_save, sender=Product)
def move_uploaded_image(sender, instance, created, **kwargs):
    if created and instance.image:
        # Récupérer le chemin complet de l'image téléchargée
        image_path = instance.image.path
        
        # Définir le nouveau chemin de destination dans le répertoire statique
        static_image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', os.path.basename(image_path))
        
        # Déplacer l'image téléchargée vers le répertoire statique
        os.rename(image_path, static_image_path)