from footballTeam import FootballTeam as FT


teamsPoints = {}

with open('task_1_in.txt') as file:
    print('INPUT:\n')

    # чтение количества матчей
    matchesCount = int(file.readline())

    for i in range(matchesCount):
        # чтение результа матча
        team1, team1goals, team2, team2goals = file.readline().replace('\n', '').split()
        team1goals, team2goals = map(int, (team1goals, team2goals))
        print(team1, team1goals, team2, team2goals)

        # проверка, есть ли команда в словаре
        if team1 not in teamsPoints.keys():
            teamsPoints[team1] = FT()
        if team2 not in teamsPoints.keys():
            teamsPoints[team2] = FT()

        # подсчёт очков
        if team1goals == team2goals:
            teamsPoints[team1].draws += 1
            teamsPoints[team2].draws += 1
        else:
            if team1goals > team2goals:
                teamsPoints[team1].wins += 1
                teamsPoints[team2].loses += 1
            else:
                teamsPoints[team2].wins += 1
                teamsPoints[team1].loses += 1

print('\n\nANSWER:\n')

for key in teamsPoints.keys():
    print(f'{key}: {str(teamsPoints[key])}')


