#
#	PLOTRAWPG
#		Plot raw pan genome (if it is small)
#		as a sequence of characters, using
#		matplotlib.
#
##################################################

#!/bin/bash

source ./config.sh

python ${source}/plotRawPG.py \
	--inputLabel $1 \
	--inputPath ${data}/rawPanGenomes/
