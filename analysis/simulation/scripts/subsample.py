from itertools import combinations
from sklearn.metrics.cluster import adjusted_rand_score
import numpy as np
 
# report % bins correctly classified to the xth largest cluster
copynumber_file = "/Users/gillianchu/mek/cnaviz/simulations/zenodo_dataset/data/noWGD/dataset_n2_s4669/tumor/copynumbers.csv"
truth_file = "/Users/gillianchu/mek/cnaviz/simulations/hatchet-paper/simulation/data/noWGD/dataset_n2_s4669/k4_01090_02008_00506035_00504055_cn_annotated_maxmin.bb"
inferred_file = "/Users/gillianchu/mek/cnaviz/simulations/hatchet-paper/simulation/free/noWGD/dataset_n2_s4669/k4_01090_02008_00506035_00504055/hatchet/hatchet.seg.ucn_cn_annotated_maxmin.bb"
edited_file = "/Users/gillianchu/mek/cnaviz/simulations/hatchet-paper/simulation/free/noWGD/dataset_n2_s4669/k4_01090_02008_00506035_00504055/hatchet/edited/hatchet.seg.ucn_20211231120537.tsv"

truth_sampled_file = "/Users/gillianchu/mek/cnaviz/simulations/scripts/hatchet/rand_index_n2_s4669/truth_sampled.bb" 
inferred_sampled_file = "/Users/gillianchu/mek/cnaviz/simulations/scripts/hatchet/rand_index_n2_s4669/inferred_sampled.bb"
edited_sampled_file = "/Users/gillianchu/mek/cnaviz/simulations/scripts/hatchet/rand_index_n2_s4669/edited_sampled.bb"

def proc_pair(s):
	c1, c2 = s.split('|')
	c1, c2 = int(c1), int(c2)
	return (min(c1, c2), max(c1, c2))

def read_cn_file(f):
	print("Hardcoded to 2 clones")
	cluster_diff = set()
	with open(f, "r") as r:
		lines = r.readlines()
		cluster_id = 0
		for line in lines[1:]:
			chrm, start, end, clone0, clone1 = line.split()
			clone0, clone1 = proc_pair(clone0), proc_pair(clone1)
			if clone0 != clone1:
				cluster_diff.add(cluster_id)	
			cluster_id += 1
	return cluster_diff

def read_file(f, diffset): 
	# returns the list of bins (chrm, start, end) that fall in diffset clusters
	print("Reading %s..." % f)
	print("Diff set has %s clusters" % str(len(diffset)), diffset)
	binset = set()
	with open(f, "r") as r:
		lines = r.readlines()
		print("%s has %s lines." % (f, str(len(lines))))
		per_bin_clusters = []

		for i, colname in enumerate(lines[0].split('\t')):
			if colname == 'RD':
				rdr = i
			elif colname == 'BAF':
				baf = i
			elif colname == 'CLUSTER\n':
				cluster = i
		all_clusters = set()
		for line in lines[1:]:
			chrm, start, end, sample, _, _, _, _, _, _, c = line.split('\t')
			all_clusters.add(c.rstrip())
			if int(c.rstrip()) in diffset:
				binset.add((chrm, start, end))
		print("all_clusters", all_clusters)
		return binset 

def subsample_file(f, f2, binset):
	print("Reading %s..." % f)
	print("Bin set has %s bins" % str(len(binset)))
	print("Writing to %s..." % f2)
	
	with open(f, "r") as r:
		with open(f2, "w+") as w:
			lines = r.readlines()
			w.write(lines[0])
			for line in lines[1:]:
				chrm, start, end, sample, _, _, _, _, _, _, c = line.split('\t')
				if (chrm, start, end) in binset:
					w.write(line)

# read in the copy numbers file
# ID those segments with different copy numbers between the clones
cluster_diff = read_cn_file(copynumber_file)

# write those cluster IDs?

# ID the bins that fall into these cluster IDs
binset = read_file(truth_file, cluster_diff)

# write the bins?

# subsample ground truth
subsample_file(truth_file, truth_sampled_file, binset)

# subsample inferred
subsample_file(inferred_file, inferred_sampled_file, binset)

# subsample edited
subsample_file(edited_file, edited_sampled_file, binset)

print("Done.")	
