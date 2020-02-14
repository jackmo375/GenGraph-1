# Load modules
## enviroment
import argparse
## local
import ggPanGenome as ggpg
import ggPlot as ggp

# Main program
def main():

	# get file label etc from user input
	parser = argparse.ArgumentParser()
	parser.add_argument('--inputLabel', type=str, help='Label of input raw pan genome')
	parser.add_argument('--inputPath',  type=str, help='path to input raw pan genome')
	parser.add_argument('--nGenomes',  type=int, help='number of genomes to simulate')
	parser.add_argument('--avSize',  type=int, help='average size (in nucleotides) of each genome')
	parser.add_argument('--maxDist',  type=int, help='maximum numer of variants between any pair of genomes')
	args = parser.parse_args()
	
	# generate a pan genome:
	#rpg = ggpg.genPanGenome(N_n, N_g)
	rpg = ggpg.genGenomeCluster(args.avSize, args.nGenomes, 5)

	# print pan genome to a fasta file: 
	rpg.toFasta('test', fDir='../data/rawPanGenomes/')


if __name__ == '__main__':
	main()