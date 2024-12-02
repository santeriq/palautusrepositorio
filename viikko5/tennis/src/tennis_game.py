class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def tennis_scores(self, score):
        if score == 0:
            tennis_score = "Love"
        elif score == 1:
            tennis_score = "Fifteen"
        elif score == 2:
            tennis_score = "Thirty"
        elif score == 3:
            tennis_score = "Forty"

        return tennis_score
    

    def get_score(self):
        if self.player1_score == 0 and self.player2_score == 0:
            return "Love-All"
        
        elif self.player1_score == 4:
            return f"Win for {self.player1_name}"
        elif self.player2_score == 4:
            return f"Win for {self.player2_name}"

        else:
            score_1 = self.tennis_scores(self.player1_score)
            score_2 = self.tennis_scores(self.player2_score)
            return f"{score_1}-{score_2}"