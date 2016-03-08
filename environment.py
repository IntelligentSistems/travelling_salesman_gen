#!/usr/bin/python

from event import Event
from population import Population
from person import Person

class Environment():
    contrainsts = None
    turns = 1000
    convergence = 100
    population = None
    population_size = 20

    def __init__(self, contrainsts=Event(20), population_size=20, turns=100000, convergence=1000):
        self.contrainsts = contrainsts
        self.turns = turns
        self.convergence = convergence
        self.population_size = population_size


    def generatePopulation(self):
        self.population = Population(self.population_size, self.contrainsts)

    def makeNewGeneration(self):
        new_population = Population()
        elected = self.population.getTheBest()
        new_population.add(elected)

        while len(new_population) < self.population_size:
            couple = self.population.selectACouple()
            child = Person.copulate(couple['man'], couple['woman'], self.contrainsts)
            if child is not None:
                new_population.add(child)

        self.population = new_population

    def adapt(self):
        self.generatePopulation()
        for turn in range(self.turns):
            self.makeNewGeneration()
            person = self.population.getTheBest()
            print " i: "+str(turn)+" person "+str(person)
        return self.population.getTheBest()


