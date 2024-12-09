from stats import Stats
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, All, Not, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Stats(reader)

    matcher = Or(
    HasAtLeast(45, "goals"),
    HasAtLeast(70, "assists")
)

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
