from django.db import models

GAME_MAKER_MAXLEN = 50
GAME_NAME_MAXLEN = 100
GAME_DESC_MAXLEN = 150


class Game(models.Model):
    """Game Model

        Fields:
            models (CharField): The name of the game
            game_type (ForeignKey): The type of game
            description (CharField): The description of the game
            number_of_players (IntegerField): The max number of players of the game
            maker (CharField): The company that made the game
        """

    name = models.CharField(max_length=GAME_NAME_MAXLEN)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    description = models.CharField(max_length=GAME_DESC_MAXLEN)
    number_of_players = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    maker = models.CharField(max_length=GAME_MAKER_MAXLEN)
