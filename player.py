from choice import Choice


class Player:
    def __init__(self, choice=Choice.ROCK, name='Bot'):
        self.name = name
        self.choice = choice.value

    def whoWins(self, p1, p2):
        if p1.var == p2.var:
            return 'НИЧЬЯ!'
        elif p1.var == 'rock' and p2.var == 'scissors' \
                or p1.var == 'scissors' and p2.var == 'paper' \
                or p1.var == 'paper' and p2.var == 'rock':
            return f'Победил игрок с именем {p1.name}!'
        else:
            return f'Победил игрок с именем {p2.name}!'
