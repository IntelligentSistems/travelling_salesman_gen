#!/usr/bin/python

from person import Person
from random import random

class Population():
    people=[]

    def __init__(self, size=None, constriants=None):
        self.people = []
        if size is not None and constriants is not None:
            for x in range(size):
                self.people.append(Person(constriants))

    def __len__(self):
        return len(self.people)

    def add(self, person):
        if person is not None:
            self.people.append(person)

    def selectPerson(self):
        sum_weights = self.calculateSumWeights()
        reverse_sum_weights = 0
        for person in self.people:
            if person is not None:
                reverse_sum_weights += sum_weights - person.weight
        
        r = random()
        acumulated_probability = 0

        selected=None

        for person in self.people:
            acumulated_probability += float(sum_weights - person.weight)/float(reverse_sum_weights)
            if r <= acumulated_probability:
                selected=person
                break

        return selected

    def calculateSumWeights(self):
        sum_weigths = 0
        for person in self.people:
            if person is not None:
                sum_weigths += person.weight
        return sum_weigths

    def selectACouple(self):

        man = self.selectPerson()
        woman = self.selectPerson()

        return {"man": man, "woman": woman}

    def getTheBest(self):
        better_person = None
        for person in self.people:
            if better_person is None or person.weight < better_person.weight:
                better_person = person
        return better_person


