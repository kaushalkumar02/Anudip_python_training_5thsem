players = []

for i in range(11):
    score = int(input(f"Player {i+1} Score: "))
    players.append(("Player " + str(i+1), score))

print("\n----- SCORECARD -----")
print("Player\t\tScore")

for i in range(11):
    print(players[i][0], "\t\t", players[i][1])
    