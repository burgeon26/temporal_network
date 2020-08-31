import csv,os
import pandas as pd
from datetime import datetime,timedelta
import networkx as nx

default_w = 1
def transgraph():
    G = nx.Graph()

    f = open('(sample)sam_tianchi_2014002_rec_tmall_log.csv','r')
    csv_reader = csv.reader(f)
    next(csv_reader)
    for line in csv_reader:
        # print(line)
        G.add_node(line[0],type='item')
        G.add_node(line[1],type='user')
        G.add_edge(line[0],line[1],action=line[2],vtime=line[3])

    # nx.write_gexf(G,'graph.gexf')
# transgraph()

def cutdata():
    # f = open('(sample)sam_tianchi_2014002_rec_tmall_log.csv','r')
    dateparse = lambda x: pd.datetime.strptime(x, '%Y/%m/%d %H:%M')

    df = pd.read_csv('(sample)sam_tianchi_2014002_rec_tmall_log.csv', parse_dates=['vtime'], date_parser=dateparse)
    # csv_reader = csv.reader(f)
    # next(csv_reader)
    # for line in csv_reader:
    start = datetime(2014,9,1)
    end = datetime(2014,9,4)
    for i in range(1,11):
        target = df[(df['vtime'] >= start) & (df['vtime'] < end)]
        target.to_csv('interval'+str(i)+'.csv',index=False)
        start = start + timedelta(days=3)
        end = end + timedelta(days=3)
# cutdata()

def ana1():
    dir = 'interval/'
    for file in os.listdir(dir):
        filepath = os.path.join(dir,file)
        f = open(filepath,'r')
        print(file,len(f.readlines())-1)
# ana1()

def takeSecond(elem):
    return elem[1]
def ana2():
    dir = 'interval/'
    for file in os.listdir(dir):
        G = nx.Graph()
        filepath = os.path.join(dir, file)
        f = open(filepath,'r')
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            G.add_node(line[0], type='item')
            G.add_node(line[1], type='user')
            if G.has_edge(line[0], line[1]):
                G[line[0]][line[1]]['weight'] += default_w
            else:
                G.add_edge(line[0], line[1], weight=default_w,action=line[2])
        # print(G.degree(weight='weight'))
        # print(G.degree('i314',weight='weight'))
        x = list(G.degree(weight='weight'))
        x.sort(key=takeSecond, reverse=True)
        print(x[0:20])
        # print(nx.degree_histogram(G))
# ana2()

def ana3():
    dir = 'interval/'
    for file in os.listdir(dir):
        G = nx.Graph()
        filepath = os.path.join(dir, file)
        f = open(filepath,'r')
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            G.add_node(line[0], type='item')
            G.add_node(line[1], type='user')
            if G.has_edge(line[0], line[1]):
                G[line[0]][line[1]]['weight'] += default_w
            else:
                G.add_edge(line[0], line[1], weight=default_w,action=line[2])
        # print(G.adj['u39'])   #求解u39连接边权重
        # print(sorted(G['u39'].items(), key=lambda edge: edge[1]['weight'],reverse=True))

        d={'click':0,'cart':0,'collect':0,'alipay':0}   #边行为统计
        # print(G.edges())
        for i in list(G.edges()):
            if G.get_edge_data(i[0],i[1])['action']=='click':
                d['click']+=1
            elif G.get_edge_data(i[0],i[1])['action']=='cart':
                d['cart'] += 1
                # print(i)
            elif G.get_edge_data(i[0],i[1])['action']=='collect':
                d['collect']+=1
            else:
                d['alipay']+=1
        print(d)
# ana3()

def ana4():
    df = pd.read_csv('sim.csv')
    df = df.sort_values('sim',ascending = False)
    df.to_csv('sim_sort.csv',index=False)
# ana4()