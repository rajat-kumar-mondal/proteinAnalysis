# proteinAnalysis (version 1)
`proteinAnalysis` is a Python package developed at Biochemistry & Bioinformatics Lab, Department of Applied Sciences, Indian Institute of Information Technology Allahabad (IIIT-A), Devghat, Jhalwa, Prayagraj-211015, U. P. India.

This package is written in pure Python to compute very basic composition of a protein sequence.

## Introduction
It is very important to know the compositional details for any kind of protein-related study. The composition of a protein plays a crucial role in determining its type (hydrophobic or hydrophilic), activity, and behavior. This package can be used to find various compositional details of a protein. This package does not compute the count of all amino acids and their frequencies, as this function is already implemented in the `ProteinAnalysis` class in the `ProtParam` module of the `biopython` package. Except for amino acid count and frequency, other compositional details can be computed by this package.

## Development Background
The development of this package was part of the **Anti-microbial Peptide Database version 1 (AMPDB v1)** project, which has been published in **Nature Scientific Reports** by **Nature Publishing Group UK**. Click on the DOI in the citation section below to see the article.

## Requirements
Python 3.10 or higher versions required.

## Features
The `proteinAnalysis` package has the following features:

1. The package is written in pure Python. No built-in Python modules are required for this package.
2. The package is free for academic users and can be distributed freely. For commercial use, users must contact the author.
3. The package can analyze various compositions of a protein sequence.
4. There is no limitation on the size of the protein sequence.

The package can compute the following:

1. Missing Amino Acid(s)
2. Most Occurring Amino Acid(s)
3. Less Occurring Amino Acid(s)
4. Hydrophobic Amino Acid(s) Count
5. Hydrophilic Amino Acid(s) Count
6. Basic Amino Acid(s) Count
7. Acidic Amino Acid(s) Count
8. Modified Amino Acid(s) Count
9. Modified Amino Acid(s) Frequencies

## Download the package
The package can be downloaded by right-clicking the link and selecting 'Save link as...'.

## Usage Example
```python
# import the package
from proteinAnalysis import proteinAnalysis as pan

# take a protein sequence
seq = 'GAVLIUXGAA'

# create an object of the class and pass the sequence
panObj = pan(seq)

# call methods to print the composition details of the sequence
print(panObj.missingResidues())
print(panObj.mostOccuringResidues())
print(panObj.lessOccuringResidues())
print(panObj.hydrophobicAACount())
print(panObj.hydrophilicAACount())
print(panObj.acidicAACount())
print(panObj.basicAACount())
print(panObj.modifiedAACount())
print(panObj.modifiedAAFrequency())
```

## Citation
**Mondal, R.K., Sen, D., Arya, A., and Samanta, S.K., 2023.** Developing anti-microbial peptide database version 1 to provide comprehensive and exhaustive resource of manually curated AMPs. *Scientific Reports, 13(1), p.17843.*  
**DOI:** [https://doi.org/10.1038/s41598-023-45016-3](https://doi.org/10.1038/s41598-023-45016-3)
