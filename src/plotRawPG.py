# load modules
## enviroment
import argparse
## local
import ggPanGenome as ggpg
import ggPlot as ggpt

def main():

	# get file label from user input
	parser = argparse.ArgumentParser()
	parser.add_argument('--inputLabel', type=str, help='Label of input raw pan genome')
	parser.add_argument('--inputPath',  type=str, help='path to input raw pan genome')
	parser.add_argument('--outLabel', type=str, help='Label of output figure')
	parser.add_argument('--outPath',  type=str, help='path to output figure')
	args = parser.parse_args()

	print(args.outPath)

	# read data from sequence file
	rpg = ggpg.fromFasta(args.inputLabel, args.inputPath)

	# plot using matplot lib
	ggpt.plotRawPanGenome(rpg, fLabel=args.outLabel, fDir=args.outPath)

if __name__ == '__main__':
	main()