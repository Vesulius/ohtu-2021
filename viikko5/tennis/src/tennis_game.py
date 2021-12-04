SCORES = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = {
            "name": player1_name,
            "score": 0
        }
        self.player2 = {
            "name": player2_name,
            "score": 0
        }

    def won_point(self, player_name):
        if player_name == self.player1["name"]:
            self.player1["score"] = self.player1["score"] + 1
        else:
            self.player2["score"] = self.player2["score"] + 1

    def get_score(self):
        if self.player1["score"] == self.player2["score"]:
            return self.even_game()
        elif max(self.player1["score"], self.player2["score"]) < 4:
            return self.mid_game()
        return self.end_game()

    def even_game(self):
        if self.player1["score"] < 4:
            return f"{SCORES[self.player1['score']]}-All"
        return "Deuce"

    def mid_game(self):
        return f"{SCORES[self.player1['score']]}-{SCORES[self.player2['score']]}"

    def end_game(self):
        minus_result = self.player1["score"] - self. player2["score"]

        if minus_result == 1:
            return f"Advantage {self.player1['name']}"
        if minus_result == -1:
            return f"Advantage {self.player2['name']}"
        if minus_result >= 2:
            return f"Win for {self.player1['name']}"
        return f"Win for {self.player2['name']}"
