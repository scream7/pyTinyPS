import sys
sys.path.append('../pyTinyPS')
from consthash import ConsistentHashing

ch = ConsistentHashing()
for i in range(10):
	ip= '192.168.0.' + str(i)
	ch.add_node(ip)

val = '192.168.0.2'
for i in range(10):
	print ch.get(val + str(i))
