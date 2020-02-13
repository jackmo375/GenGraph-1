# Load modules
## enviroment
## local
import ggPanGenome as ggpg
import ggPlot as ggp

# Main program
def main():

	N_g = 5		# number of genomes
	N_n = 30	# number of nucleotides
	
	# generate a pan genome:
	#rpg = ggpg.genPanGenome(N_n, N_g)
	rpg = ggpg.genGenomeCluster(N_n, N_g, 5)

	# print pan genome to a fasta file: 
	rpg.toFasta('test', fDir='../data/rawPanGenomes/')


if __name__ == '__main__':
	main()