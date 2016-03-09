#!/usr/bin/python

from random import randint
from file import File

class Event():
	graph=None
	min=0
	
	def __init__(self, filename=None, size=4, max_weight=10):
		if filename is None:
			self.graph = [[randint(1,max_weight) for x in range(size)] for y in range(size)]
			for i in range(size):
				self.graph[i][i] = -1
		else:
			self.graph = File(filename).graph
		
	
	def __str__(self):
		out = " i "
		for x in range(len(self.graph)):
			out += " "+str(x)+" "
		out += "\n"
		for x in range(len(self.graph)):
			out += " "+str(x)+"  "+str(self.graph[x])+"\n"
		
		return out

	def __len__(self):
		return len(self.graph)
	

	def f(self, path, isSolution=True):
		source = path[0]
		weight = 0
		
		for destiny in path:
			if destiny != source:
				value = self.graph[source][destiny]
				if value < self.min:
					return None
				weight += value

			source = destiny
		
		if isSolution:
			destiny = path[0]
			weight += self.graph[source][destiny]

		return weight
	
	def getInitialSolution(self):
		solution=[]
		numbers_of_vertex = len(self.graph)
 		count = 0

		while len(solution) < numbers_of_vertex:
			vertex = randint(0,numbers_of_vertex-1)
			while vertex in solution:
				vertex = randint(0,numbers_of_vertex-1)
			solution.append(vertex)
			if len(solution) == numbers_of_vertex:
				if self.f(solution, True) is None:
					solution.pop()
					count += 1
				else:
					count = 0
			else:
				if self.f(solution, False) is None:
					solution.pop()
					count += 1
				else:
					count = 0

			if count == 2:
				solution = []

		return solution
