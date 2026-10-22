class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, player):
        self.player = player

player1 = Player("Alex")
team1 = Team(player1)
team2 = Team(player1)