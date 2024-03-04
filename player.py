from choice import Choice


class Player:
    def __init__(self, choice=Choice.ROCK, name='Bot'):
        self.name = name
        self.choice = choice.value # .value для получения значения из перечисления

    def whoWins(self, p2): # self передает значения по умолчанию
        if self.choice == p2.choice:
            return 'НИЧЬЯ!'
        elif self.choice == 'rock' and p2.choice == 'scissors' \
                or self.choice == 'scissors' and p2.choice == 'paper' \
                or self.choice == 'paper' and p2.choice == 'rock':
            return f'Победил игрок с именем {self.name}!'
        else:
            return f'Победил игрок с именем {p2.name}!'
