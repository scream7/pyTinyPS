import traceback
import sys

class ConsistentHashing(object):
	def __init__(self,hash_func=hash, num_replicas=1):
		self.__hash=hash_func
		self.__numReplicas=num_replicas
		self.__hashCircle={}
		self.__keys=[]

	def keys(self):
		return self.__keys
	def hash_circles(self):
		return self.__hashCircle
	def node_size(self):
		return len(self.__hashCircle)

	def add_node(self,node):
		try:
			if not isinstance(node, str):
				raise TypeError("The type of node should be str.")
		except TypeError:
			traceback.print_exc(file=sys.stdout)

		for i in xrange(self.__numReplicas):
			replicasNode = node + str(i)
			keyNode = self.__hash(replicasNode)
			self.__hashCircle[keyNode] = node
			self.__keys.append(keyNode)
		self.__keys.sort()

	def remove_node(self,node):
		try:
			if not isinstance(node, str):
				raise TypeError("The type of node should be str.")
		except TypeError:
			traceback.print_exc(file=sys.stdout)

		for i in xrange(self.__numReplicas):
			replicasNode = node + str(i)
			keyNode = self.__hash(replicasNode)
			del self.__hashCircle[keyNode]
			self.__keys.remove(keyNode)

	def get(self,val):
		if self.node_size()==0:
			return None
		keyVal = self.__hash(val)
		nodeLength = self.node_size()
		for i in xrange(nodeLength):
			if int(keyVal) < int(self.__keys[i]):
				return self.__hashCircle[self.__keys[i]]
		return self.__hashCircle[self.__keys[0]]