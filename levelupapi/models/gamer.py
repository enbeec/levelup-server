from django.db import models
from django.contrib.auth.models import User

GAMER_BIO_MAXLEN = 50


class Gamer(models.Model):
    """Gamer Model

        Fields:
            models (OneToOneField): The user information for the gamer
            bio (CharField): The bio of the user
        """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=GAMER_BIO_MAXLEN)
