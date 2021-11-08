import statistics
import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_finds_right_player(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")

    def test_search_returns_none_if_player_not_found(self):
        self.assertIsNone(self.statistics.search("Noone"))

    def test_team_gives_right_results(self):
        list = self.statistics.team("EDM")
        self.assertEqual(len(list), 3)
        for player in list:
            self.assertEqual(player.team, "EDM")

    def test_top_scorers_right_order(self):
        list = self.statistics.top_scorers(2)
        self.assertEqual(len(list), 3)
        self.assertEqual(list[0].name, "Gretzky")
        self.assertEqual(list[1].name, "Lemieux")

