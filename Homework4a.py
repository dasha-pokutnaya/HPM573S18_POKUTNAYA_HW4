from enum import Enum
import numpy as np

class currentside(Enum):
    """ heads or tails outcome of coin flip  """
    HEADS = 0
    TAILS = 1

class Game(object):
    def __init__(self, id):
        self._id = id
        self._totalFlips = 20
        self._flipNumber = 1
        self._currentside = currentside.TAILS
        self._tailscount = 0
        self._wincount = 0
        self._rnd = np.random # random number generator for this patient
        self._rnd.seed(self._id * self._flipNumber)  # specifying the seed of random number generator for this patient

    def nextFlip(self):
        if self._currentside == currentside.TAILS:
            if self._rnd.random_sample() < 0.5:
                if self._tailscount >= 2:
                    self._wincount += 1
                self._currentside = currentside.HEADS
                self._tailscount = 0

            if self._rnd.random_sample() > 0.5:
                self._currentside = currentside.TAILS
                self._tailscount += 1

        elif self._currentside == currentside.HEADS:
            if self._rnd.random_sample() < 0.5:
                self._currentside = currentside.HEADS
                self._tailscount = 0
            if self._rnd.random_sample() > 0.5:
                self._currentside = currentside.TAILS
                self._tailscount = 1

        self._flipNumber += 1

    def Game(self):
        for i in range(1, self._totalFlips+1): # we started at one so we need to go one past 20.
            self._rnd = np.random
            self._rnd.seed(self._id * self._flipNumber)
            self.nextFlip()

    def payout(self):
        self.Game()
        self._payout = -250 + (100*self._wincount)
        return self._payout

class Cohort:
    def __init__(self, id, pop_size):
        self._players = []
        n = 1

        while n <= pop_size:
            player = Game(id=id * pop_size + n)
            self._players.append(player) # adding each player to your list
            n += 1

    def simulate(self):
        game_reward = []
        for player in self._players:
            game_reward.append(player.payout())
        return sum(game_reward)/len(game_reward)


trial1 = Cohort(id=1, pop_size=1000)
print(trial1.simulate())
