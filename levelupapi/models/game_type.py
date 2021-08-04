from django.db import models

GAMETYPE_LABEL_MAXLEN = 50


class GameType(models.Model):
    """GameType model

        Fields:
            label (CharField): name of the game type
        """
    label = models.CharField(max_length=GAMETYPE_LABEL_MAXLEN)
