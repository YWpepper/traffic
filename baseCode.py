import pandas as pd
import numpy as np
import networkx as nx

edges = pd.DataFrame()
edges['sources'] = [1,1,1,2,2,3,3,4,4,5,5,5]
edges['targets'] = [2,4,5,3,1,2,5,1,5,1,3,4]
edges['weights'] = [1,1,1,1,1,1,1,1,1,1,1,1]

G = nx.from_pandas_edgelist(edges, source = 'sources', target = 'targets' , edge_attr = 'weights')

#degree
print(nx.degree(G))
