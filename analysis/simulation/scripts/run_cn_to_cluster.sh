#!/bin/sh

if false; then
	true_datadir="/Users/gillianchu/mek/cnaviz/simulations/hatchet-paper/simulation/data/noWGD/*"
	#true_datadir="/Users/gillianchu/mek/cnaviz/simulations/zenodo_dataset/data/noWGD/*"
	for d in ${true_datadir}; do
		echo $d
		for f in $d/*.bb.gz ; do
			echo "f, $f"
			echo "cn, $d/tumor/copynumbers.csv"
			outfile=${f%.*}_cn_annotated_maxmin.bb
			if [ -f "$outfile" ]; then
				echo "$outfile already exists."
			else
				echo "$outfile doesn't exist."
				open $f
				sleep 1
				#python true_cn2cluster.py ${f%.*} $d/tumor/copynumbers.csv
				#rm ${f%.*}
			fi

		done
	done
fi

if true; then
	# k4_01090_02008_00506035_00504055/hatchet/hatchet.seg.ucn.gz
	est_datadir="/Users/gillianchu/mek/cnaviz/simulations/hatchet-paper/simulation/free/noWGD/*"
	for d in ${est_datadir}; do
		#echo "d, $d"
		for f in ${d}/* ; do
			#echo "f, $f"
			for ff in $f/hatchet/hatchet.seg.ucn.gz ; do
				echo "ff, $ff"
				outfile=${ff%.*}_cn_annotated_maxmin.bb
				echo "outfile, $outfile"
				if [ -f "$outfile" ]; then
					echo "$outfile already exists."
				else
					#rm $outfile
					echo "$outfile doesn't exist."
					open $ff
					echo "PASSING ${ff%.*}"
					sleep 1
					python est_cn2cluster.py ${ff%.*} $outfile
					rm ${ff%.*}
					#find "$f/hatchet/" -type d -name 'noWGD*' -prune -print -exec rm -rf {} + 
				fi
			done
		done
	done
fi


