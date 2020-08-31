import csv
from community import community_louvain
import networkx as nx

default_w = 1
def transgraph():
    G = nx.Graph()
    f = open('(sample)sam_tianchi_2014002_rec_tmall_log.csv','r')
    csv_reader = csv.reader(f)
    next(csv_reader)

    for line in csv_reader:
        G.add_node(line[0], type='item')
        G.add_node(line[1], type='user')
        if G.has_edge(line[0], line[1]):
            G[line[0]][line[1]]['weight'] += default_w
        else:
            G.add_edge(line[0], line[1], weight=default_w)
    # 求解所有的商品节点
    items = []
    for n in G.nodes():
        if G.nodes[n]['type']=='item':
            items.append(n)

    # 形成user-user网络
    for item in items:
        neighbors = list(G[item].keys())
        for u1 in neighbors:
            for u2 in neighbors:
                i = neighbors.index(u1)
                j = neighbors.index(u2)
                w = G[item][u1]['weight'] + G[item][u2]['weight']
                if i<j:
                    if G.has_edge(u1, u2):
                        G[u1][u2]['weight'] += w
                    else:
                        G.add_edge(u1, u2, weight=w)
        G.remove_node(item)
    # 社团发现
    partition = community_louvain.best_partition(G)
    print(partition)
    for user in partition.keys():
        G.nodes[user]['partition']=partition[user]
    # print(G.nodes['u2625'])
    nx.write_gexf(G, 'graph2.gexf')
transgraph()