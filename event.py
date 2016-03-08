#!/usr/bin/python

from random import randint

class Event():
	graph=None
	
	def __init__(self, size=4, max_weight=10):
		self.graph = [[randint(1,max_weight) for x in range(size)] for y in range(size)]
		for i in range(size):
			for j in range(size):
				if i == j:
					self.graph[i][j] = 0
	
	def __str__(self):
		out = " i "
		for x in range(len(self.graph)):
			out += " "+str(x)+" "
		out += "\n"
		for x in range(len(self.graph)):
			out += " "+str(x)+" "+str(self.graph[x])+"\n"
		
		return out
		
	
	def f(self, solution):
		source = solution[0]
		weight = 0
		
		for destiny in solution:
			weight += self.graph[source][destiny]
			source = destiny
		
		destiny = solution[0]
		weight += self.graph[source][destiny]

		return weight
	
	
	def getInitialSolution(self):
		solution=[]
		numbers_of_vertex = len(self.graph)
 
		for i in range(numbers_of_vertex):
			vertex = randint(0,numbers_of_vertex-1)
			while vertex in solution:
				vertex = randint(0,numbers_of_vertex-1)
			solution.append(vertex)

		return solution
