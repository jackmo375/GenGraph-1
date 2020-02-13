#
#	GETDATA
#		pull data from eg NCBI ftp repo
#
#	options:
#		+ bat corona virus (use ./getData.sh batCorona
#
#########################################################

#!/bin/bash

. ./config.sh

label=$1

# download raw fasta files:

wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Viruses/bat_coronavirus_1a_uid29247/NC_010437.ffn
mv NC_010437.ffn ${data}/rawPanGenomes/${label}0.ffn

wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Viruses/bat_coronavirus_bm48_31_bgr_2008_uid51751/NC_014470.ffn
mv NC_014470.ffn ${data}/rawPanGenomes/${label}1.ffn

wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Viruses/bat_coronavirus_cdphe15_uid215863/NC_022103.ffn
mv NC_022103.ffn ${data}/rawPanGenomes/${label}2.ffn

wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Viruses/bat_coronavirus_hku10_uid177902/NC_018871.ffn
mv NC_018871.ffn ${data}/rawPanGenomes/${label}3.ffn

wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Viruses/bat_coronavirus_uid385635/NC_034440.ffn
mv NC_034440.ffn ${data}/rawPanGenomes/${label}4.ffn

# create sequence file for input to GenGraph:

sequenceFile=${data}/rawPanGenomes/${label}.seq.tsv

## print headers
echo -e "seq_name\taln_name\tseq_path\tannotation_path" > $sequenceFile

## print entries:
echo -e "NC_010437\tseq0\t"${cwd}/${label}0.ffn"\tNA"	>> $sequenceFile
echo -e "NC_014470\tseq1\t"${cwd}/${label}1.ffn"\tNA"	>> $sequenceFile
echo -e "NC_022103\tseq2\t"${cwd}/${label}2.ffn"\tNA"	>> $sequenceFile
echo -e "NC_018871\tseq3\t"${cwd}/${label}3.ffn"\tNA"	>> $sequenceFile
echo -e "NC_034440\tseq4\t"${cwd}/${label}4.ffn"\tNA"	>> $sequenceFile



