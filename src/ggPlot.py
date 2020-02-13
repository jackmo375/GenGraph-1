#
#	Library of functions to handle 
#	general  plotting
#	of genome data
#
#######################################

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

def plotRawPanGenome(pg, fname=None, show=True):

	fig, ax = plt.subplots()

	createDataPlot(pg, fig, ax)

	ax.set_yticks(range(pg.nGenomes))
	ax.set_xlabel('nucleotides')
	ax.set_ylabel('genomes')
	plt.tight_layout()

	if fname is not None:
		plt.savefig(fname)

	if show is True:
		plt.show()


def createDataPlot(pg, fig, ax):

	n_p = len(panGenome[:,0])
	n_g = len(panGenome[0,:])

	im = ax.imshow(panGenome, cmap="Dark2")

	for i in range(n_p):
		for j in range(n_g):
			text = ax.text(j, i, ggpg.NUCL_VEC[panGenome[i, j]],
				ha="center", va="center", color="w")

	ax.set_xticks([])
	ax.set_yticks([])

	fig.tight_layout()