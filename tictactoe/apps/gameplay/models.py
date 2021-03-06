from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q # enables logical operators

GAME_STATUS_CHOICES = (
    ('F', 'First player to move'),
    ('S', 'Second player to move'),
    ('W', 'First player wins'),
    ('L', 'Second player wins'),
    ('D', 'Draw')
)


class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        # lists all games that user is in
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        # list all games that are still on-going
        return self.filter(
            Q(status='F') | Q(status='S')
        )

    def draw(self):
        # list all games that ended in draw
        return self.filter(Q(status='D'))


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="game_first_player", on_delete=models.DO_NOTHING)
    second_player = models.ForeignKey(User, related_name="game_second_player", on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

    objects = GamesQuerySet.as_manager()
    def __str__(self):
        return '{0} vs {1}'.format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=100, blank=True)
    by_first_player = models.BooleanField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return 'x: {0} y: {1}'.format(self.x, self.y)

