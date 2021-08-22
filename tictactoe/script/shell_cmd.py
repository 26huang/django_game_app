# shell command examples after running
# $python manage.py shell

from apps.gameplay.models import Game, Move

# view Game object and fields
Game.objects.all()
g = Game.objects.all(pk=1)
g.last_active

# change and save values
g.status = 'S'
g.save()

# filter results
Game.objects.filter(status='F')
Game.objects.exclude(status='F')
Game.objects.filter(second_player__username='wei')

# insert new data
m = Move(x=0, y=1, comment='GL!', by_first_player=True, game=g)
m.save()

# get game info
m.game
g.move_set
g.move_set.all()
g.move_set.count()
g.move_set.exclude(comment='')

# delete a record
g = Game.objects.get(pk=1)
g.delete()