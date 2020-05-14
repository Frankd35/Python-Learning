class GameStat:
    """record statistic"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.life_limit = 7
        self.game_play = False
        self.ship_life = self.life_limit
        self.kill = 0
        self.new_life = 0
        self.score = 0
        self.alien_value = 5
