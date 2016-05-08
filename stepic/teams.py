n = int(input())
teams = []
team = []
wins = {}
draw = {}
games = {}
results = {}
for i in range(n):
    team = input().split(';')
    teams.append(team)

for i in teams:
    if i[0] not in wins:
        wins[i[0]] = 0
        draw[i[0]] = 0
        games[i[0]] = 0
    if i[2] not in wins:
        wins[i[2]] = 0
        draw[i[2]] = 0
        games[i[2]] = 0
    if i[1] > i[3]:
        wins[i[0]] += 1
    elif i[1] == i[3]:
        draw[i[0]] += 1
        draw[i[2]] += 1
    else:
        wins[i[2]] += 1
    games[i[0]] += 1
    games[i[2]] += 1
for i in games.keys():
    results[i] = []
    results[i].append(games[i])
    results[i].append(wins[i])
    results[i].append(draw[i])
    lose = games[i] - wins[i] - draw[i]
    points = (wins[i] * 3) + draw[i]
    results[i].append(lose)
    results[i].append(points)
for key in results.keys():
    d = str(key)
    d = d+':'
    print(d,end="")
    for j in results[key]:
        print(j,end=' ')
    print(end='\n')
