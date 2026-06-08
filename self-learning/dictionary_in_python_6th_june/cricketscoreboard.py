# --------------------------------------------------
# Problem Statement:
# Analyze cricket player scores and perform the following:
# 1. Display players who scored 50 or more runs.
# 2. Count the number of centuries (100 or more runs).
# 3. Find the player with the highest score.
# 4. Create a list of players scoring below 30 runs.
# 5. Determine how many players scored between 50 and 99.
# --------------------------------------------------
# Sample Data
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether scores is a dictionary
if not isinstance(scores, dict):
    print("Invalid data: Scores should be stored in a dictionary.")
    is_valid = False

# Validate player names and scores
if is_valid:
    for player, runs in scores.items():

        # Player name must be a string
        if not isinstance(player, str):
            print("Invalid player name found.")
            is_valid = False
            break

        # Runs must be numeric
        if not isinstance(runs, (int, float)):
            print(f"Invalid score for {player}.")
            is_valid = False
            break

        # Runs cannot be negative
        if runs < 0:
            print(f"Negative score found for {player}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Players scoring 50 or more runs
    fifty_plus = [
        player for player, runs in scores.items()
        if runs >= 50
    ]

    # Count centuries
    centuries = sum(
        1 for runs in scores.values()
        if runs >= 100
    )

    # Highest scorer
    highest_scorer = max(scores, key=scores.get)
    highest_score = scores[highest_scorer]

    # Players scoring below 30 runs
    below_30 = [
        player for player, runs in scores.items()
        if runs < 30
    ]

    # Players scoring between 50 and 99
    between_50_99 = sum(
        1 for runs in scores.values()
        if 50 <= runs <= 99
    )

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Players who scored 50 or more runs:")
    print(fifty_plus)

    print("\nNumber of centuries:")
    print(centuries)

    print("\nHighest scorer:")
    print(f"{highest_scorer} - {highest_score}")

    print("\nPlayers scoring below 30 runs:")
    print(below_30)

    print("\nNumber of players scoring between 50 and 99:")
    print(between_50_99)