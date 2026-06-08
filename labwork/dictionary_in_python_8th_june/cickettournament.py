# --------------------------------------------------
# Problem Statement:
# Runs scored by players in a tournament are stored as:
# Perform analysis on the given runs dictionary.
# --------------------------------------------------
# Sample Data
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}
# --------------------------------------------------
# Processing Section
# --------------------------------------------------

# 1. Players scoring more than 500 runs
above_500 = [player for player, score in runs.items() if score > 500]

# 2. Orange Cap winner (highest scorer)
top_player = max(runs, key=runs.get)
top_runs = runs[top_player]

# 3. Lowest scorer
low_player = min(runs, key=runs.get)
low_runs = runs[low_player]

# 4. Total runs scored
total_runs = sum(runs.values())

# 5. Players scoring below 400
below_400 = [player for player, score in runs.items() if score < 400]

# 6. Players scoring between 400 and 600
between_400_600_count = sum(1 for score in runs.values() if 400 <= score <= 600)

# --------------------------------------------------
# Output Section
# --------------------------------------------------

print("Players Scoring More Than 500 Runs:", *above_500)

print("\nOrange Cap Winner:")
print(f"{top_player} ({top_runs})")

print("\nLowest Scorer:")
print(f"{low_player} ({low_runs})")

print("\nTotal Tournament Runs:")
print(total_runs)

print("\nPlayers Scoring Below 400:", below_400)

print("\nPlayers Between 400 and 600 Runs:", between_400_600_count)