# -*- coding: utf-8 -*-
""" Basic IPD game space implementation """

from kernel.space.basicSpaces import Space


class IpdGame(Space):
    """ Abstract Market """
    STRATEGY = ['C', 'D']
    PAYOFFS = {'CC': [4, 4],
               'CD': [0, 7],
               'DC': [7, 0],
               'DD': [1, 1]}

    def __init__(self, 
                 model, 
                 name, 
                 variables
                 ):
        """ Intialize abstract market """
        super().__init__(model, 
                         name, 
                         variables
                         )
        self.players = []

   
    def update(self):
        """ Update game space """
        self.matching()
        self.play()


    def matching(self):
        """ Match the agents in pairs"""
        agents  = list(self.model.mixed_agents())
        half = len(agents) // 2
        players1 = agents[:half]
        players2 = agents[half:]
        self.players = zip(players1, players2)

    def play(self):
        """ Here the players play the game """
        for player1, player2 in self.players:
                    player1.select_game(player2)
                    player2.select_game(player1)
                    p1 = player1.play()
                    p2 = player2.play()
                    game = p1 + p2
                    player1.game_payoff(player2.name, p2,
                                        self.PAYOFFS[game][1],
                                        self.PAYOFFS[game][0]
                                        )
                    player2.game_payoff(player1.name, p1, 
                                        self.PAYOFFS[game][0],
                                        self.PAYOFFS[game][1]
                                        )
 
  

