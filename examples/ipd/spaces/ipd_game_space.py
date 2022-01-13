# -*- coding: utf-8 -*-
""" Basic IPD game space implementation """

from space.basicSpaces import Space


class IpdGame(Space):
    """ Abstract Market """
    STRATEGY = ['C', 'D']
    PAYOFFS = {'CC': [3, 3],
               'CD': [0, 5],
               'DC': [5, 0],
               'DD': [1, 1]}

    def __init__(self, model, name, actions_set_file, action_class, variables):
        """ Intialize abstract market """
        super().__init__(model, name, actions_set_file, action_class, variables)

    def update(self):
        """ here the players play the game """
        agents = list(self.model.mixed_agents())
        half = len(agents) // 2
        players1 = agents[:half]
        players2 = agents[half:]
        for player1 in players1:
            if len(players2) > 0:
                player2 = players2.pop()
                p1 = player1.play()
                p2 = player2.play()
                game = p1 + p2
                player1.game_payoff(player2.name, p2,
                                    self.PAYOFFS[game][1],
                                    self.PAYOFFS[game][0]
                                    )
                player2.game_payoff(player1.name,
                                    p1, self.PAYOFFS[game][0],
                                    self.PAYOFFS[game][1]
                                    )
            else:
                player1.game_payoff("NA", 0)
