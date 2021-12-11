from statistics import Statistics
from player_reader import PlayerReader
from matchers import *
from query_builder import QueryBuilder


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder(All())
    matcher = (
        query
        .playsIn("NYR")
        .hasFewerThan(10, "goals")
        .hasAtLeast(5, "goals")
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
