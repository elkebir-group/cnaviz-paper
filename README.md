## CNAViz-data

This is the data repository for [CNAViz](https://github.com/elkebir-group/cnaviz). The live tool can be found [here](https://elkebir-group.github.io/cnaviz/). 

```
|
|– analysis
|   |— casasent:
|	|- driver_genes: .ipynb notebooks to create linear plots and genes, also including a file for driver genes 
|   	|— hatchet: .ini files to run HATCHet
|	    |- output_PX: output files after running HATCHet with the HATCHet clustering, where X is the patient number
|	    |- output_HPX: output files after running HATCHet with the HATCHet + CNAViz refined clustering,  where X is the patient number 
|   |- simulation:
|   	| - ascat: files to calculate rand index
| 	| - denovo: CNAViz clustering of n2_s4669 from scratch
|	| - hatchet: files to calculate rand index
|	| - scripts: helpful scripts to calculate V-measure, rand, and ipynb notebooks for plotting linear and scatter plots
|
|— data
|   |— casasent: data can be found on the NCBI Sequence Read Archive (SRA) under accession numbers [SRP114962](https://www.ncbi.nlm.nih.gov/sra/?term=SRP114962) and [SRP116771](https://www.ncbi.nlm.nih.gov/sra/?term=SRP116771).  
|   |— simulation/n2_s4669: Details on the simulated data can be found [here](https://github.com/raphael-group/hatchet-paper)
|	|- free: inferred copy numbers after running HATCHet
|	|- ground_truth_noWGD: ground truth copy numbers  
```

Screencasts:
- [Demo Video](https://youtu.be/nU8DTJIJEZ4)
- Simulated Data (`n2_s4669`):
	- [De novo clustering](https://youtu.be/FHmFomNjb5E)
	- [HATCHet + CNAViz](https://youtu.be/7_S-KM-PDfI)
	- [ASCAT + CNAViz](https://youtu.be/YtfEvFoNCNk) 


Input Segmentations to CNAViz:
- Simulated (`n2_s4669`)
	- [HATCHet Input](https://github.com/elkebir-group/cnaviz-paper/blob/master/analysis/simulation/hatchet/rand_index_n2_s14584/hatchet.seg.ucn_cn_annotated_maxmin.bb)
	- [ASCAT Input](https://github.com/elkebir-group/cnaviz-paper/blob/master/analysis/simulation/ascat/rand_index_n2_s4669/s4669_aspcf_cnavizin.txt)
	- [HATCHet + CNAViz Output](https://github.com/elkebir-group/cnaviz-paper/blob/master/analysis/simulation/hatchet/rand_index_n2_s4669/hatchet.seg.ucn_20211231120537.tsv)
	- [ASCAT + CNAViz Output](https://github.com/elkebir-group/cnaviz-paper/blob/master/analysis/simulation/ascat/rand_index_n2_s4669/k4_01090_02008_00506035_00504055_cn_annotated_maxmin.bb)

- Real Casasent Data
	- [HATCHet Input](https://github.com/elkebir-group/cnaviz-paper/blob/master/analysis/Casasent/hatchet/output_P5/results/best.seg.ucn)
		- For a patient `X`, the input data can be found at `analysis/Casasent/hatchet/output_PX/results/best.seg.ucn`. The link is provided to Patient 5. 
	- [HATCHet + CNAViz Output](https://github.com/elkebir-group/cnaviz-paper/tree/master/analysis/Casasent/hatchet/output_HP5_v4/bbc)
		- For a patient `X`, the output data can be found at `analysis/Casasent/hatchet/output_HPX_v*/bbc/bulk.bbc`. The `bulk.seg` file in the same folder is computed from the `.bbc` file using the `segment_bins.py` script in the `/hatchet` folder. The link is provided to Patient 5.  


We use existing software [ASCAT](https://github.com/VanLoo-lab/ascat) and [HATCHet](http://compbio.cs.brown.edu/hatchet/README.html#usage). 


