import matplotlib.pyplot as plt 
import networkx as nx
import numpy as np
from sklearn.manifold import TSNE

## Copy from https://github.com/palash1992/GEM/blob/master/gem/evaluation/visualize_embedding.py

def plot_embedding(node_pos, node_colors=None, di_graph=None):
    node_num, embedding_dimension = node_pos.shape
    if(embedding_dimension > 2):
        print "Embedding dimensiion greater than 2, use tSNE to reduce it to 2"
        model = TSNE(n_components=2)
        node_pos = model.fit_transform(node_pos)

    if di_graph is None:
        # plot using plt scatter
        plt.scatter(node_pos[:,0], node_pos[:,1], c=node_colors)
    else:
        # plot using networkx with edge structure
        pos = {}
        for i in xrange(node_num):
            pos[i] = node_pos[i, :]
        if node_colors:
            nx.draw_networkx_nodes(di_graph, pos, node_color=node_colors, width=0.1, node_size=100, arrows=False, alpha=0.8, font_size=5)
        else:
            nx.draw_networkx(di_graph, pos, node_color=node_colors, width=0.1, node_size=300, arrows=False, alpha=0.8, font_size=12)
    plt.show()

def read_graph(graph_path,weighted,directed):
    '''
    Reads the input network in networkx.
    '''
    if graph_path.split('.')[-1] == 'gml':
        G = nx.read_gml(graph_path)
        for edge in G.edges():
            G[edge[0]][edge[1]]['weight'] = 1
        return G

    if weighted:
        G = nx.read_edgelist(graph_path, nodetype=int, data=(('weight',float),), create_using=nx.DiGraph())
    else:
        G = nx.read_edgelist(graph_path, nodetype=int, create_using=nx.DiGraph())
        for edge in G.edges():
            G[edge[0]][edge[1]]['weight'] = 1

    if not directed:
        G = G.to_undirected()

    return G

def load_embedding(file_name):
    with open(file_name, 'r') as f:
        n, d = f.readline().strip().split()
        X = np.zeros((int(n)+1, int(d)))
        for line in f:
            emb = line.strip().split()
            emb_fl = [float(emb_i) for emb_i in emb[1:]]
            X[int(emb[0]),:] = emb_fl
    return X

