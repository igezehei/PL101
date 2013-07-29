#!/usr/bin/python

""" Since the list is not hashable in the graph search, I change to tuple"""

from utils import *;
from search import *;

class EightPuzzle(Problem):
	"""The problem of solving a eight puzzle problem """
	def __init__(self, state):
		self.initial = tuple(state)
				
	def successor(self, state):
		"""In the 8 puzzle problem, move the blank to other position."""
		result = []
		position = list(state).index(0)	
		for action, newposition in self.possible_position(position).iteritems():
			new = list(state[:])
			new[newposition], new[position] = new[position], new[newposition]
			result.append((action, tuple(new)))
		return result
		
	def possible_position(self, position):
		"""return the possible position"""
		result = {};
		col = position % 3;
		row = position // 3;
		# add the action in a circle manner. No dead iter now
		if row != 2:
			result['D'] = position +3
		if col != 0: 
			result['L'] = position -1	
		if row != 0:
			result['U'] = position -3
		if col != 2:
			result['R'] = position +1

		return result
	"""	
		if col == 0:
			result['R'] = position+1
			#result.append('D': position+1)
		elif col ==1:
			result['L'] = position-1
			result['R'] = position+1
			#result.append(position+1)
			#result.append(position-1)
		else:
			result['L'] = position-1
			#result.append(position-1)
		
		if row == 0:
			result['D'] = position+3;
			#result.append(position+3)
		elif row ==1:
			result['U'] = position-3;
			result['D'] = position+3;
			#result.append(position+3)
			#result.append(position-3)
		else:
			result['U'] = position-3;
			#result.append(position-3)
		return result;
	"""

	def goal_test(self, state):
		if state[0] != 0:
			return False
		elif state[1] !=1:
			return False
		elif state[2] !=2:
			return False
		elif state[3] !=3:
			return False
		elif state[4] !=4:
			return False
		elif state[5] !=5:
			return False
		elif state[6] !=6:
			return False
		elif state[7] !=7:
			return False
		elif state[8] !=8:
			return False
		else:
			print state
			return True 	
			# print state
	
	def h(self, node):
		"""Heuristic function"""
		# print node.state
		temp=list(node.state)
		sum=0
		for x in range(8):	# mahatten distance
			sum = sum + abs(temp.index(x)-x)
		return sum

	def h2(self, node):
		"""bad h"""
		sum = 0
		pos = 0
		for x in node.state:
			sum = sum + abs(x - pos)
			pos = pos + 1
		return sum

if (__name__=="__main__"):

#	state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
	state = [7, 2, 4, 5, 0, 6, 8, 3, 1]
#	state = (2, 6, 4, 7, 0, 3, 5, 8, 1)
	instance = EightPuzzle(state)
#  breadth_first_tree_search(instance)
	#depth_first_tree_search(instance)
#	breadth_first_graph_search(instance)
#	print depth_first_graph_search(instance).path()
	print astar_search(instance, instance.h).path()
