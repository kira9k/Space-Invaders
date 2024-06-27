class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализаци статистики"""
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """статистика, изменяющаяся во время игры"""
        self.guns_left = 3
        self.score = 0
