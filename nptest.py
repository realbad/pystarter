import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

rows1 = np.array(['154'])
# for i in range(26):
#     print(chr(ord('a')+ i))
alpha = ['a', 'b', 'c', 'd', 'e', 'f']
num = [i for i in range(1,17)]
# rows2 = [alp+str(i)+',' for alp in alpha for i in num]
nodes = [alp+str(i) for alp in alpha for i in num]
rows2=[]
rows2.append(nodes)
# rows2 = np.array(['c9','c10','c11','c12','c13'])
# print(rows1)
# row=np.append(rows2)
print(rows2[0])
G = nx.MultiDiGraph()
G.add_nodes_from([2,3])
# G.add_path([0,1,2,3])
G.add_path([10,11,12],weight=7)
# G.add_edges_from([(1,2),(1,3)])
nx.draw_spring(G)
plt.show()