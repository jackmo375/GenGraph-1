#
#	GENERATE
#		Generate raw pan genome for input into GenGraph
#
###########################################################

#!/bin/bash

# load useful shell variables:
source ./config.sh

# user input parameters:
label=$1

# prepare target output directory:
if ls ${data}/rawPanGenomes/${label}* 1> /dev/null 2>&1; then
	rm ${data}/rawPanGenomes/${label}*
fi

# run the program with parameters:
python ${source}/generate.py \
	--inputLabel $label \
	--inputPath ${data}/rawPanGenomes/ \
	--nGenomes 10 \
	--avSize 50 \
	--maxDist 5

