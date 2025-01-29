LEADERBOARD_FILE = "leaderboard.txt"

def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            leaderboard = []
            for line in file.readlines():
                name, score = line.strip().split(" - ")
                leaderboard.append({"name": name, "score": int(score)})
            return leaderboard
    except FileNotFoundError:
        return []


def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        for entry in leaderboard:
            file.write(f"{entry['name']} - {entry['score']}\n")


def update_leaderboard(player_name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({"name": player_name, "score": score})
    leaderboard.sort(key=lambda x: x['score'], reverse=True)  # Sortiere nach Punktzahl absteigend
    save_leaderboard(leaderboard)


def display_leaderboard():
    leaderboard = load_leaderboard()
    print("\n=== Leaderboard ===")
    for idx, entry in enumerate(leaderboard, 1):
        print(f"{idx}. {entry['name']} - ${entry['score']:,}")
    print("====================\n")