# Описывает результаты одной команды
class FootballTeam:
    wins = 0
    draws = 0
    loses = 0

    def get_total_games(self):
        return self.wins + self.draws + self.loses

    def get_points(self):
        return self.wins * 3 + self.draws * 1

    def __str__(self):
        return f'{self.get_total_games()} {self.wins} {self.draws} {self.loses} {self.get_points()}'