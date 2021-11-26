# -*- coding: utf-8 -*-
""" Household Agents from the basic macroeconomic model """

from .agents import EconomicAgent
from .agents_accounting import Good, House
import random


class Household(EconomicAgent):
    """ Household Agent """

    SPACE = 'CreditMarket'


    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.first_step = True
        self.house = House("house",owner_of_g=None, producer_of_g=None)
        self.demanded_house = House("house",owner_of_g=self, producer_of_g=self)
        self.my_market = self.spaces[self.SPACE]
        self.can_bid = False
    

    def step(self):
        """ Household Agent Step method """
        if self.first_step:
            #self.my_ownership = random.choices(self.house_ownership,
            #                                   self.ownership_probability)
            self.house_ownership = "renter"
            self.define_demmanded_house()
            self.first_step = False

        self.calculate_income()
        self.consume()
        self.housing_decision()
        self.generate_offer()
        self.got_house()
        self.pay_contracts()
        self.pay_taxes()

    def define_demmanded_house(self):
        """ The agent defines the demanded house type and value"""
        self.my_house_type = random.choices(self.house.QUALITY,
                                               self.house_type_probability)
        self.house.quality = self.my_house_type
            
        ## demand house
        self.demanded_house.quality = self.my_house_type
        self.demanded_house.value_of_g = self.savings

    
    def calculate_income(self):
        """ Households receive income according to 
            an appropriate distribution throughout life and age
        
            A renda das famílias advêm das seguintes fontes:
        
            Y = I + T + M
        
            I = Renda do trabalho;
            T = Transferências Governamentais;
            M = Ganhos de Capital.
        """
        ### Government transfers and capital gains will be included
        
        self.current_income = self.labor_income  
        self.labor_income = self.labor_income * 1.003 # upgrading labor income to test it
 
    def consume(self):
        """
            Households use a percentage of income in essential consumption
        
            Todas as Famílias realizam gastos de sua renda conforme equação:
        
            Y = C + F + R + S (2)

            C = Gasto Não-Habitacional (aqui é substituido por um percentual da renda);
            F = Financiamento Imobiliário (mortgage);
            R = Aluguel (value percentage of income);
            S = Poupança.

            Ou S = Y - (C + F + R)

            E C = cY (c = consumption_rate)
        
        """
        self.consumption = self.current_income * self.consumption_rate
        self.current_expenditure = self.consumption + self.rent + self.mortgage
        self.current_savings = self.current_income - self.current_expenditure
        self.savings += self.current_savings

    def housing_decision(self):
        """ 
            The agent have financial_availability?
               yes
               The agent have enough wealth?
                   yes: make_bid
        """

        self.calculate_financial_availability()
        self.calculate_PV()
        self.calculate_finacial_liability()

        ### Housing Decision
        if (self.availability_limit >= self.financial_availability):
           #and (self.savings >= self.financial_liability)):
           self.can_bid = True
        else:
            self.can_bid = False
    
    def generate_offer(self):
        "Agent generates offer"
        if self.can_bid:
            self.my_market.bid_market("D", self.demanded_house)


    def got_house(self):
        ### Tem erro aqui - CHECAR
        """ The household have bought a house """
        if self.demand_satisfied and self.house_ownership != 'owner':
            self.house = self.contracted_offers
            self.house.owner_of_g = self
            self.savings -= self.house.value_of_g
            self.house_ownership = 'owner'


    def pay_contracts(self):
        """ Tenants pay rent. Owners with financing pay the bank. """
        pass


    def pay_taxes(self):
        """ The HH pay taxes to the government """
        pass

    def got_contract(self):
        """ The household bought a house """
        pass

    def release_bid(self):
        """ The agent have a house """
        pass

    def calculate_financial_availability(self):
        """ 
        A Disponibilidade Financeira (D) é definida pela soma dos gastos com R
        (Aluguel 2 ) e S (Poupança) que será disponibilizada para pagamento da
        prestação do financiamento imobiliário. A (D) em cada período deve ser
        superior a 30% para se tornar “elegível” na aquisição de um imóvel.
        Assim, temos:
                        D=(1−(C + F)/Y)∗100
        """
        self.financial_availability = 1 - self.current_expenditure/self.current_income

        return self.financial_availability

    def calculate_PV(self):
        """ The agent calculate the house present value """

        D = self.financial_availability
        Y = self.current_income
        i = self.interest_rate
        n = self.number_of_payments

        self.PV = Y * D * (((1+ i)**n - i) / ((1 + i)**n * i))
        
        return self.PV

    def calculate_finacial_liability(self):
        """ The financial liability is que percentage of the house PV 
            regulated by the financial authority or bank
             E = m.PV
        """
        self.financial_liability = self.macroprudential_policy * self.PV

        return self.financial_liability
