from itertools import combinations
from sklearn.metrics.cluster import v_measure_score 
import numpy as np
 
# report % bins correctly classified to the xth largest cluster

#truth_file = "/Users/gillianchu/mek/cnaviz/simulations/hatchet-paper/simulation/data/noWGD/dataset_n2_s4669/k4_01090_02008_00506035_00504055_cn_annotated_maxmin.bb"
#inferred_file = "/Users/gillianchu/mek/cnaviz/simulations/hatchet-paper/simulation/free/noWGD/dataset_n2_s4669/k4_01090_02008_00506035_00504055/hatchet/hatchet.seg.ucn_cn_annotated_maxmin.bb"
#edited_file = "/Users/gillianchu/mek/cnaviz/simulations/hatchet-paper/simulation/free/noWGD/dataset_n2_s4669/k4_01090_02008_00506035_00504055/hatchet/edited/hatchet.seg.ucn_20211231120537.tsv"

truth_file = "/Users/gillianchu/mek/cnaviz/simulations/scripts/ascat/rand_index_n2_s4669/k4_01090_02008_00506035_00504055_cn_annotated_maxmin.bb"
inferred_file = "/Users/gillianchu/mek/cnaviz/simulations/scripts/denovo/s4669_20220111142154.tsv"
edited_file = "/Users/gillianchu/mek/cnaviz/simulations/scripts/denovo/s4669_20220111142154.tsv"

#inferred_file = "/Users/gillianchu/mek/cnaviz/simulations/scripts/ascat/rand_index_n2_s4669/s4669_aspcf_cnavizin.txt"
#edited_file = "/Users/gillianchu/mek/cnaviz/simulations/scripts/ascat/rand_index_n2_s4669/s4669_20220110033110.tsv"

def read_file(f): 
	# returns the read_file for each of the clusters in this file
	print(f)
	with open(f, "r") as r:
		lines = r.readlines()
		print(len(lines), "number of lines")
		print(lines[0].split('\t'))
		per_bin_clusters = []
		for i, colname in enumerate(lines[0].split('\t')):
			if colname == 'RD':
				rdr = i
			elif colname == 'BAF':
				baf = i
			elif colname == 'CLUSTER\n':
				cluster = i
		for line in lines:
			per_bin_clusters.append(line.split('\t')[cluster].strip())
		return per_bin_clusters

def rand_index(labels):
	bin_idx = [i for i, _ in enumerate(labels)]
	print(len(bin_idx), "number of bins")
	bin_combs = list(combinations(bin_idx, 2))

	same = 0
	diff = 0
	for idx1, idx2 in bin_combs:
		label1, label2 = labels[idx1], labels[idx2]
		#print(label1, label2)
		if label1 == label2:
			same += 1
		else:
			diff += 1
	return (same + diff) / len(bin_combs)
			
	
# read in the ground truth file
true_cluster_label = read_file(truth_file) 
print("true cluster label")
#print(true_cluster_label)

# read in the inferred file
infer_cluster_label = read_file(inferred_file) 

# read in the newly corrected inferred file
edit_cluster_label = read_file(edited_file) 

# calculate sum error distance between the nearest read_file
#print(true_cluster_label)
#print(infer_cluster_label) 

infer_dst = v_measure_score(true_cluster_label, infer_cluster_label)
print("Inferred v measure:", infer_dst)

edit_dst = v_measure_score(true_cluster_label, edit_cluster_label)
print("Edited v measure:", edit_dst)
	
#true_R = rand_index(true_cluster_label)
#infer_R = rand_index(infer_cluster_label)
#edit_R = rand_index(edit_cluster_label)
#print("true, infer, edit")
#print(true_R, infer_R, edit_R)
