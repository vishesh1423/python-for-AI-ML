players = []
runs = []

for i in range(3):
  player = input("enter player name-->")
  run = int(input("enter your run-->"))

  players.append(player)
  runs.append(run)

  print(players)
  print(runs)


players_runs = dict(zip(players,runs))
print(players_runs)


max = runs[0]
average = sum(runs)/3


for i in range(3):
  if runs[i] > max:

    player = players[i]
    max = runs[i]

print("maximum run is -->" , max)


print("average runs is -->" , average)
