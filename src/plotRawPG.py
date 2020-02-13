# load modules
## enviroment
import argparse
## local
import ggPanGenome as ggpg

def main():

	# get file label from user input
	parser = argparse.ArgumentParser()
	parser.add_argument('--inputLabel', type=str, help='Label of input raw pan genome')
	parser.add_argument('--inputPath',   type=str, help='path to input raw pan genome')
	args = parser.parse_args()

	# read data from sequence file
	ggpg.fromFasta(args.inputLabel, args.inputPath)

	# plot using matplot lib

if __name__ == '__main__':
	main()