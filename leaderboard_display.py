# Leaderboard Display Utility
# Author: Aashi Asati
# Hacktoberfest 2025
# Description: Fixes PR model to display leaderboard data properly

def display_leaderboard(players):
    """
    Display the leaderboard sorted by score in descending order.
    Input: list of dictionaries -> [{'name': str, 'score': int}, ...]
    """
    if not players:
        print("⚠️ No players found in the leaderboard.")
        return

    # Sort players by score descending
    players_sorted = sorted(players, key=lambda x: x['score'], reverse=True)

    print("\n🏆 Leaderboard 🏆")
    print(f"{'Rank':<5} {'Player Name':<20} {'Score':<5}")
    print("-" * 35)

    for rank, player in enumerate(players_sorted, start=1):
        print(f"{rank:<5} {player['name']:<20} {player['score']:<5}")

def main():
    # Example data - can be replaced with actual PR model data
    leaderboard_data = [
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 87},
        {"name": "Charlie", "score": 92},
        {"name": "David", "score": 85},
    ]

    # Display the leaderboard
    display_leaderboard(leaderboard_data)

if name == "main":
    main()
