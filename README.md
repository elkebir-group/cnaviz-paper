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
- Simulated Data (`n2_s4669`):
	- [De novo clustering](https://youtu.be/-qsI2Bl1TXA) 
	- [HATCHet + CNAViz](https://youtu.be/X95U7DjUVzQ)
	- [ASCAT + CNAViz](https://youtu.be/lYKLyNePrQY)

We use existing software [ASCAT](https://github.com/VanLoo-lab/ascat) and [HATCHet](http://compbio.cs.brown.edu/hatchet/README.html#usage). 


