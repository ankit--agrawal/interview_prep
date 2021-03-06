#-------------------------create a node-----------------------
class Node:
	def __init__(self,value):
		self.left = None
		self.data = value
		self.right = None
#-------------------------create tree-------------------------
class Tree:
	def createNode(self,data):
		return Node(data)
	def insertNode(self,node,data):
		if node is None:
			return self.createNode(data)
		else:
			#if data less that parent node, put it on the left side
			if data < node.data:
				node.left = self.insert(node.left,data)
			#if data greater than parent node, put it on the right side
			elif data > node.data:
				node.right = self.insert(node.right,data)
			else:
			node = self.insert(node,data)
		return node

#------------------------------main----------------------------------------------

