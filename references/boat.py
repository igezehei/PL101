#!/usr/bin/python

from utils import *;
from search import *;

"""state is a tuple with (#m1, #m2, #s1, #s2, where_is_the_boat)"""
# Too many values to unpack...
# I really need a dict as the successor state....


class Boat(Problem):
	def __init__(self, state):
		self.initial = tuple(state)
		self.N = state[0]
		self.nodenum = 1

	def successor(self, state):
		result = []
		symbol = state[4]*2 -1; # 0 => -1
		action = 0
		for x in (0, 1, 2):
			for y in (0, 1, 2):
				if x + y >= 1 and x + y <= 2:
					new = (state[0] + symbol*x, state[1]-symbol*x, state[2] + symbol*y, state[3] - symbol*y, 1 - state[4])
					if self.check(new):
						result.append((action, new))
						action = action + 1
		self.nodenum = self.nodenum + action
		print result
		return result
	
	def check(self, state):
		for x in state[:-1]:
			if x<0:
				return False;

		if state[0]!=0 and state[0] < state[2]: return False;
		if state[1]!=0 and state[1] < state[3]: return False;
		
		return True


	def goal_test(self, state):
		if state[0] == 0 and state[1] == self.N and state[2] == 0 and state[3] == self.N and state[4] ==1:
			print state
			return True 	
		return False;
	
	def h(self, node):
		return 0
		state=node.state
		return state[0]

if (__name__=="__main__"):

	state=[3, 0, 3, 0, 0]

	instance = Boat(state)
#	breadth_first_tree_search(instance)
#	depth_first_tree_search(instance)
#	breadth_first_graph_search(instance)
#	depth_first_graph_search(instance)
	astar_search(instance, instance.h)
	print instance.nodenum
