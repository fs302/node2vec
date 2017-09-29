from utils import read_graph, load_embedding, plot_embedding
import argparse

def parse_args():
	'''
	Parses the node2vec arguments.
	'''
	parser = argparse.ArgumentParser(description="Run node2vec.")

	parser.add_argument('--graph', nargs='?', default='graph/karate.edgelist',
	                    help='Input graph path')

	parser.add_argument('--emb', nargs='?', default='emb/karate.emb', help='Input emb path')
	parser.add_argument('--weighted', dest='weighted', action='store_true',
	                    help='Boolean specifying (un)weighted. Default is unweighted.')
	parser.add_argument('--unweighted', dest='unweighted', action='store_false')
	parser.set_defaults(weighted=False)

	parser.add_argument('--directed', dest='directed', action='store_true',
	                    help='Graph is (un)directed. Default is undirected.')
	parser.add_argument('--undirected', dest='undirected', action='store_false')
	parser.set_defaults(directed=False)
	return parser.parse_args()


def main(args):
	G = read_graph(args.graph, args.weighted, args.directed)
	emb = load_embedding(args.emb)
	plot_embedding(emb,node_colors=None,di_graph=G)

if __name__ == "__main__":
	args = parse_args()
	main(args)
