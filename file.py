#!/usr/bin/python

class File():
	fileRef = "Default"
	matrixSize = 0
	graph = []
	def __init__(self, fileName):
		num = []
		graph = []
		with open(fileName, 'r') as f:
			graphSize = int(f.readline())
			for line in f:
				for s in line.split():
					temp = int(s)
					if temp == 9999:
						temp = -1
					num.append(temp)
					if len(num) == graphSize:
						graph.append(num)
						num = []			
				#print str(num)
				#print len(num)
				
		self.graph = graph



