# Modules
## enviroment
import networkx as nx
import time
## local
import gengraph as gg

def main():

	args = getInputArguments()

	if args.toolkit == 'make_genome_graph':
		make_genome_graph(args)


def getInputArguments():
	'''
	Get user input arguments from script call
	'''

	parser = gg.argparse.ArgumentParser(
		description='''Welcome to GenGraph v0.1''', 
		epilog="""Tools for the creation and use of graph genomes""")

	parser.add_argument('toolkit', type=str, default='test_mode', help='Select the tool you would like to use')
	parser.add_argument('--out_file_name', type=str, help='Prefix of the created file')
	parser.add_argument('--out_file_path', type=str, default='./', help='Output file destination')
	parser.add_argument('--alignment_file', nargs=1, help='The path to the alignment file')
	parser.add_argument('--backbone_file', nargs=1, default='default', help='The path to the backbone file')
	parser.add_argument('--out_format', nargs=1, default='default', help='Format for the output')
	parser.add_argument('--block_aligner', nargs=1, default=['progressiveMauve'], help='Block aligner to use')
	parser.add_argument('--progressiveMauve_path', nargs=1, default=['progressiveMauve'], help='Path to progressiveMauve if not in PATH')
	parser.add_argument('--node_msa_tool', nargs=1, default='mafft', help='MSA tool to use')
	parser.add_argument('--seq_file', type=str, help='Tab delimited text file with paths to the aligned sequences')
	parser.add_argument('--no_seq', dest='should_add_seq', action='store_false',
						help='Create a graph genome with no sequence stored within')
	parser.add_argument('--make_circular', type=str, default='No',
						help='To circularise the graph for a sequence, give the name of that sequence')
	parser.add_argument('--recreate_check', dest='rec_check', action='store_true',
						help='Set to True to attempt to recreate the input sequences from the graph and compare to the originals')
	parser.add_argument('--extract_sequence', type=str, default='some_isolate',
						help='To circularise the graph for a sequence, give the name of that sequence')
	parser.add_argument('--isolate', type=str, default='some_isolate', help='pass the isolate variable. For graph generation, this should be the genome that best represents the ancesteral state.')
	parser.add_argument('--extract_sequence_range', nargs=2, default=['all', 'all'],
						help='Extract sequence between two positions')
	parser.add_argument('--graph_file', type=str, help='Give the path to the graph file')
	parser.add_argument('--max_node_length', type=int, default=-1, help='Max sequence length that can be aligned')
	parser.add_argument('--input_file', type=str, help='Generic input')
	parser.add_argument('--locus_ID', type=str, help='The name of the gene or feature')

	parser.set_defaults(should_add_seq=True)
	parser.set_defaults(rec_check=False)

	return parser.parse_args()


def make_genome_graph(args):
	'''
	1. Read in a collection of fasta files, specificed in a sequence file,
	2. store as a modified networkx object, 
	3. then print genome graph to an xml file. 

	Requires:
		--out_file_name
		--seq_file

	Optional:
		--recreate_check
		--no_seq
	'''
	# simplify variable names:
	global_aligner = args.block_aligner
	local_aligner = args.node_msa_tool
	path_to_progressiveMauve = args.progressiveMauve_path[0]
	
	# start timer for benchmarking etc:
	start_time = time.time()
	
	parsed_input_dict = gg.parse_seq_file(args.seq_file)

	# Initial global alignment of genome graph:
	if args.block_aligner[0] == 'progressiveMauve' and args.backbone_file == 'default':
		print('Conducting progressiveMauve')
		gg.logging.info(parsed_input_dict)
		gg.progressiveMauve_alignment(path_to_progressiveMauve, parsed_input_dict[2], args.out_file_path, args.out_file_name)

	# conversion to block graph:
	if args.backbone_file == 'default':
			bbone_file = args.out_file_path + 'globalAlignment_' + args.out_file_name + '.backbone'
	else:
		print('Using existing BBone file')
		bbone_file = args.backbone_file[0]
	genome_aln_graph = gg.bbone_to_initGraph(bbone_file, parsed_input_dict)
	gg.refine_initGraph(genome_aln_graph)
	gg.add_missing_nodes(genome_aln_graph, parsed_input_dict)
	nx.write_graphml(genome_aln_graph, args.out_file_path + 'intermediate_Graph.xml')

	# node splitting:
	if args.max_node_length != -1:
		genome_aln_graph = split_all_long_nodes(genome_aln_graph, args.max_node_length)
		print('Nodes split')
		nx.write_graphml(genome_aln_graph, args.out_file_path + 'intermediate_split_Graph.xml')

	# local node re-alignment:
	print('Conducting local node realignment')

	genome_aln_graph = gg.realign_all_nodes(genome_aln_graph, parsed_input_dict, out_file_path=args.out_file_path)
	gg.add_graph_data(genome_aln_graph)
	genome_aln_graph = gg.link_all_nodes(genome_aln_graph)

	print('Genome graph created')

	# save the genome graph to file:
	out_put_dir = args.out_file_path
	if args.out_file_path[-1] != '/':
		out_put_dir += '/'

	if args.out_format == 'default':

		out_filename_created = out_put_dir + args.out_file_name + '.xml'
		nx.write_graphml(genome_aln_graph, out_filename_created)

	if args.out_format[0] == 'serialize':
		print('Writing to serialized file')
		pickle.dump(genome_aln_graph, open(out_put_dir + args.out_file_name + '.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

	end_time = (time.time() - start_time)

	print("run time: " + str(end_time))
	gg.generate_graph_report(genome_aln_graph, out_put_dir + args.out_file_name)


if __name__ == '__main__':
	main()