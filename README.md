# BiodivTab
* BiodivTab is a domain spcific tabular data benchmark for semantic table annotation tasks.
* It is based on biodiversity research data and data augmentation and consists of 50 tables.
* Target Knowledge Graph (KG) is **Wikidata**
* It is made avaiable for participants of [SemTab 2021 challenge](https://www.cs.ox.ac.uk/isg/challenges/sem-tab/2021/index.html), Round 3.
* Involved anotation tasks are 
  * CEA - Cell Entity Annotation, matches individual cells to entities from knowledge graph
  * CTA - Column Type Annotation, assigns a semantic column type.

## Citation 
`
@inproceedings{biodivTab,
	title={{BiodivTab: A Tabular Benchmark based on Biodiversity Research Data}},
	author={Abdelmageed, Nora and Schindler, Sirko and K{\"o}nig-Ries, Birgitta},
	booktitle={SemTab@ISWC, submitted},
	year={2021}
}
`

## Datasets Citation
* The following is the datasets citation per data source.
* Not all the used datasets have a citiation, we make the use of the avaiable only 
### BExIS datasets

`@dataset{bexis_24867,
	author       = {Boeddinghaus, Runa and
	Marhan, Sven and 
	Berner, Doreen and
	Boch, Steffen and 
	Fischer, Markus and 
	Kattge, Jens and 
	Klaus, Valentin and 
	Kleinebecker, Till and 
	Oelmann, Yvonne and 
	Prati, Daniel and 
	Sch{\"a}fer, Deborah and 
	Sch{\"o}ning, Ingo and 
	Schrumpf, Marion and 
	Sorkau, Elisabeth and 
	Kandeler, Ellen and 
	Manning, Pete and 
	Kandeler, Ellen },
	title        = {{Plant functional trait shifts explain concurrent changes in the structure and function of grassland soil microbial communities}},	
	year         = 2017,
	publisher    = {Biodiversity Exploratories Information System},
	version      = 2,
	doi          = {10.25829/bexis.24867-1.1.23},
}`

`@dataset{bexis_25126,
	author       = {
	Fischer, Markus and
	Nauss, Thomas and		
	Tschapka, Marco and
	Weisser, Wolfgang and
	M{\"u}ller, J{\"o}rg	
	},
	title        = {{Aggregated species richness and habitat heterogeneity variables for testing the habitat-heterogeneity hypothesis, 2006-2018 }},	
	year         = 2020,
	publisher    = {Biodiversity Exploratories Information System},
	version      = 2,
	doi          = {10.25829/bexis.25126-1},
}`

`@dataset{bexis_25786,
	author       = {
	Seibold, Sebastian  and
	Go{\"s}ner, Martin and
	Simons, Nadja and
	Bl{\"u}thgen, Nico and
	M{\"u}ller, J{\"o}rg and
	Ambarli, Didem and
	Ammer, Christian and
	Bauhus,	Juergen and
	Fischer, Markus and 
	F{\"u}rstenau, Cornelia and		
	Habel, Jan C. and
	Linsenmair, Karl Eduard and
	Nauss, Thomas and
	Ostrowski, Andreas  and		
	Penone,	Caterina and
	Prati, Daniel and
	Schall, Peter and
	Schulze, Ernst-Detlef and
	Vogt, Juliane and
	W{\"o}llauer, Stephan and
	Weisser, Wolfgang	
	},
	title        = {{Arthropod data from 150 grassland plots, 2008-2017, and 140 forest plots, 2008-2016, used in "Arthropod decline in grasslands and forests is associated with drivers at landscape level", Nature }},	
	year         = 2019,
	publisher    = {Biodiversity Exploratories Information System},
	version      = 3,
	doi          = {10.25829/bexis.25786-1.3.11},
}`

`@dataset{bexis_27226,
	author       = {
	Leonhardt, Sara and
	Peters, Birte and		
	Keller, Alexander	
	},
	title        = {{Trap nesting solitary bee species measured on all grassland VIPs 2017-2018 }},	
	year         = 2020,
	publisher    = {Biodiversity Exploratories Information System},
	version      = 4,
	doi          = {10.25829/bexis.27226-4},
}`

`@dataset{bexis_27227,
	author       = {
	Leonhardt, Sara and
	Peters, Birte and		
	Keller, Alexander 	
	},
	title        = {{Fatty acids in pollen of Osmia bicornis larval provisions 2017-2018}},	
	year         = 2020,
	publisher    = {Biodiversity Exploratories Information System},
	version      = 2,
	doi          = {10.25829/bexis.27227-2},	
}`

`@dataset{bexis_27228,
	author       = {
	Leonhardt, Sara and
	Peters, Birte and		
	Keller, Alexander 	
	},
	title        = {{Amino acids in pollen of Osmia bicornis larval provisions 2017-2018}},	
	year         = 2020,
	publisher    = {Biodiversity Exploratories Information System},
	version      = 2,
	doi          = {10.25829/bexis.27228-4},
}`

### BEF-China

`@Article{befchina_staab,
	author       = {
	Staab, M. and
	Schuldt, A. and 
	Assmann, T. and 
	Bruelheide, H. and
	Klein, A.M.	
	},
	title        = {{Ant community structure during forest succession in a subtropical forest in South-East China}},	
	year         = 2014,
	publisher    = {Acta Oecologica},
	issue      = 61,
	pages = {32--40},
}`

`@dataset{befchina_wubet,
	author       = {
	Wubet, T. and
	Wu, Y.T. and 
	Buscot, F.	
	},
	title        = {{Soil Fungal metagenome from 12 CSPs based on the fungal ITS rDNA pyrotags}},	
	year         = 2013,
	publisher    = {BEF-China data portal},
	url          = {http://china.befdata.biow.uni-leipzig.de/datasets/397},
}`

`@dataset{befchina_nadrowski,
	author       = {
	Nadrowski, K.	
	},
	title        = {{Deviations from stem breaking probabilities at species level}},	
	year         = 2013,
	publisher    = {BEF-China data portal},
	url          = {http://china.befdata.biow.uni-leipzig.de/datasets/327},
}`

`@dataset{befchina_helge,
	author       = {
	Bruelheide, Helge	and
	Eichenberg,	David and
	Kr{\"o}ber,	Wenzel and
	B{\"o}hnke,	Martin and
	Ristok,	Christian
	},
	title        = {{Main Experiment: Leaf traits and chemicals from individual trees in the Main Experiment (Site A \& B)}},	
	year         = 2012,
	publisher    = {BEF-China data portal},
	url          = {https://china.befdata.biow.uni-leipzig.de/datasets/323},
}`

## Acknowledgment 
* The authors thank the Carl Zeiss Foundation for the financial support of the project \enquote{A Virtual Werkstatt for Digitization in the Sciences (P5)} within the scope of the program line \enquote{Breakthroughs: Exploring Intelligent Systems} for \enquote{Digitization - explore the basics, use applications}.
We would like to especially thank our Biodiversity experts Cornelia Fürstenau and Andreas Ostrowski for feedback on and validation of the created annotations.
Last but not least, we would like Samira Babalou for the fruitful discussion during the work.

* The tables provided in this challenge are based on real-world biodiversity research datasets, but have been adapted for the challenge.
In the form provided here, they may be used for the challenge, only.
Any publication on challenge results needs to contain citations of the underlying datasets.
The list of original datasets is available within our GitHub repository.
