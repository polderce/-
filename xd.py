from player import Player
from choice import Choice


bot = Player() # задаются аргументы по умолчанию

alex = Player(Choice.SCISSORS, 'Alex') # возможность задать свои аргументы

print(bot.whoWins(alex)) # вместо bot можно писать что угодно
