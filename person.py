#!/usr/bin/python

from random import random, randint
from names import randomName

class Person():
    dna = None
    weight = None
    name = "Default"

    def __init__(self, constraints=None):
        self.name = randomName()
        self.dna=[]
        if constraints is not None:
            self.dna = constraints.getInitialSolution()
            self.weight = constraints.f(self.dna)
    
    def __str__(self):
        return self.name+" weight: "+str(self.weight)+" dna: "+str(self.dna)

    def __fixConflit__(self, index, replace_value):
        value = self.dna[index]
        for i in range(len(self.dna)):
            if i != index and self.dna[i] == value:
                self.dna[i] = replace_value

    def mutation(self, probability=0.1):
        m = random()
        if m < probability:
            i = randint(0,len(self.dna)-1)
            i2 = randint(0,len(self.dna)-1)
            value = self.dna[i]
            self.dna[i] = self.dna[i2]
            self.dna[i2] = value
    
    def copulate(man, woman, constraints, mutation=0.01):
        child = Person()
        child.dna.extend(woman.dna)

        shift = int(len(child.dna)/2.0)*randint(0,1)
        for x in range(shift):
            i = shift+x
            value = man.dna[i]

            replace = child.dna[i]
            child.dna[i]=value
            child.__fixConflit__(i, replace)

        child.mutation(mutation)
        child.weight = constraints.f(child.dna)
        if child.weight is None:
            return None
        
        return child


