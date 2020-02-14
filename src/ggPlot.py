#
#	Library of functions to handle 
#	general  plotting
#	of genome data
#
#######################################

import numpy as np

import ggPanGenome as ggpg

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib import rcParams
rcParams['axes.linewidth'] = 2.5 # set the value globally
rcParams['axes.edgecolor'] = 'grey'
rcParams["figure.figsize"] = [10,10]
rcParams['xtick.labelsize'] = 15
rcParams['ytick.labelsize'] = 15
rcParams['xtick.color'] = 'grey'
rcParams['ytick.color'] = 'grey'
rcParams['lines.linewidth'] = 2.5
rcParams['axes.labelsize'] = 'xx-large'
rcParams['axes.labelcolor'] = 'grey'

def plotRawPanGenome(rpg, fLabel=None, fDir='./', show=True):
	'''
	plot a *very* small pan genome or DNA sequence
	as an array of nucleotide keys using matplotlib
		rpg :: RawPanGenome object
	'''

	fig, ax = plt.subplots()

	createDataPlot(rpg, fig, ax)

	ax.set_yticks(range(rpg.nGenomes))
	ax.set_xlabel('nucleotides')
	ax.set_ylabel('genomes')
	plt.tight_layout()

	if fLabel is not None:
		plt.savefig(fDir+fLabel+'.raw.png')

	if show is True:
		plt.show()


def createDataPlot(rpg, fig, ax):

	genomeLengths = [len(genome) for genome in rpg.Genomes]
	nNucleotides = max(genomeLengths)	

	# pad pan genome with zeros:
	panGenome = np.zeros([rpg.nGenomes,nNucleotides],dtype=np.int32)
	for i in range(rpg.nGenomes):
		panGenome[i,:len(rpg.Genomes[i])] = [ggpg.NUCL_VEC.index(c) for c in list(rpg.Genomes[i])]

	im = ax.imshow(panGenome, cmap="Dark2")

	for i in range(rpg.nGenomes):
		for j in range(nNucleotides):
			text = ax.text(j, i, ggpg.NUCL_VEC[panGenome[i,j]],
				ha="center", va="center", color="w")

	ax.set_xticks([])
	ax.set_yticks([])

	fig.tight_layout()