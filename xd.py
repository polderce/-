from player import Player
from choice import Choice


bot = Player()

alex = Player(Choice.ROCK, 'Alex')

print(bot.whoWins(bot, alex))