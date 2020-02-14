import random as rd

# Global variables
NUCL_VEC 	= ['-','A','C','G','T']
N_NUCL_VALS = len(NUCL_VEC)

class RawPanGenome:
	# class variables:

	def __init__(self, nGenomes, Genomes):
		# instance variables:
		self.nGenomes = nGenomes
		self.Genomes = Genomes

	# class members:
	def toFasta(self, fLabel, fDir='./'):
		for i in range(self.nGenomes):
			fName = fDir+fLabel+f"{i}"+'.fasta'
			fastaOut = open(fName, "w")
			### write comment line:
			fastaOut.write('> whole genome sequence:\n')
			### write sequence:
			writeGenome(self.Genomes[i], fastaOut)
			fastaOut.close()
		## write sequence file:
		seqOut = open(fDir+fLabel+'.seq.tsv', "w")
		### write headers:
		seqOut.write('seq_name\taln_name\tseq_path\tannotation_path\n')
		for i in range(self.nGenomes):
			seqOut.write(f"{i}\tseq{i}\t"+fDir+fLabel+f"{i}"+".fasta\tNA\n")
		seqOut.close()


# RawPanGenome custom constructors:
def genPanGenome(n_nucleotides, n_genomes):
	'''
	Generate totally random pan genome with no structure,
	where each genome is the same length
	'''
	panGenome = np.empty([n_genomes,n_nucleotides], dtype=np.int32)
	for i in range(n_genomes):
		panGenome[i,:] = genGenome(n_nucleotides)

	return RawPanGenome(n_genomes, panGenome)


def genGenomeCluster(n_nucleotides, n_genomes, max_dist):
	'''
	Generate a pan genome 'cluster', i.e. a collection of
	genomes that differ by only a few mutations,
	specified by max_dist. 
	'''

	g = genGenome(n_nucleotides)

	cluster = [[]]*n_genomes
	for i in range(n_genomes):
		if max_dist == 0:
			cluster[i] = g
		else:
			n_mutations = rd.randint(0,max_dist-1)
			mutation_loci = [rd.randint(0,n_nucleotides-1) for i in range(n_mutations)]
			cluster[i] = mutateGenome(g, mutation_loci)

	return RawPanGenome(n_genomes, cluster)


def fromFasta(fLabel, fDir):

	sequenceFile = fDir+fLabel+'.seq.tsv'
	seqStream = open(sequenceFile, 'r')
	# get header line:
	headers = seqStream.readline()
	panGenome = []
	for line in seqStream:
		pathToGenome = line.strip().split('\t')[2]
		faaStream = open(pathToGenome, 'r')
		genome = ''
		for faaLine in faaStream:
			if faaLine[0] == '>':
				pass
			else:
				genome = genome + faaLine
		panGenome = panGenome + [genome]

	return RawPanGenome(len(panGenome), panGenome)


# helper functions:
def genGenome(n_g):
	return [rd.randint(1,N_NUCL_VALS-1) for i in range(n_g)]

def mutateGenome(genome, loci):

	operations = [mutateAtLocus,insertAtLocus,deleteAtLocus]

	mutated = genome.copy()
	for i in loci:
		rd.choice(operations)(mutated,i)

	return mutated

def mutateAtLocus(genome, locus):
	genome[locus] = rd.randint(1,N_NUCL_VALS-1)

def insertAtLocus(genome, locus):
	#genome = np.insert(genome,locus,rd.randint(0,N_NUCL_VALS-1))
	genome.insert(locus,rd.randint(1,N_NUCL_VALS-1))

def deleteAtLocus(genome, locus):
	#genome = np.delete(genome, locus)
	genome.pop(locus)

def writeGenome(genome, outStream):
	#set max line length (in characters):
	MAX_LINE_LENGTH = 70
	j=1	# character counter
	for i in range(len(genome)):
		if j>MAX_LINE_LENGTH:
			outStream.write('\n')
			j=1
		else:
			outStream.write(NUCL_VEC[genome[i]])
		j += 1