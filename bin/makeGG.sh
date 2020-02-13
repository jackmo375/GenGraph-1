#
#	MAKEGG
#		make genome graph from raw pan genome
#
################################################

#!/bin/bash

# load shell variables:
. ./config.sh

# use specified data source (e.g. label=test, batCorona...):
label=$1

# run main program file:
python ${source}/makeGG.py \
	make_genome_graph \
	--seq_file ${data}/rawPanGenomes/${label}.seq.tsv \
	--out_file_path ${data}/ \
	--out_file_name ${label} \
	--recreate_check

# remove unaligned sequence files:
rm temp_*