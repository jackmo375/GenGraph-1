#
#	MAKEGG
#		make genome graph from raw pan genome
#
################################################

#!/bin/bash

# load shell variables:
source ./config.sh

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
if ls temp_* 1> /dev/null 2>&1; then
	rm temp_*
else
	echo 'makeGG.sh Error: genome graph was not generated'
fi