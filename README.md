# proteinAnalysis (version 1)
`proteinAnalysis` is a python package developed at Biochemistry & Bioinformatics Lab, Department of Applied Sciences, Indian Institute of Information Technology Allahabad (IIIT-A), Devghat, Jhalwa, Prayagraj-211015, U. P. India.

This package is written in pure python language to compute very basic composition of a protein sequence.

## Introduction
It is very important to know the compositional details for any kind of protein related study. The composition of a protein plays a crucial role to decide the type (hydrophobic or hydrophilic), activity and behaviour of a protein. This package can be use to find various compositional details of a protein. This package cannot compute the count of all amino acid and their frequencies, because this function is already implemented in `ProteinAnalysis` class in `ProtParam` module in `biopython` package. Except amino acid count and frequency other compositional details can be computed by this package.

## Requirements
python 3.10 or higher versions required.

## Features
proteinAnalysis package has the following features:

   1. The package is written in pure python language. No built-in modules in the python software is required for this package.
   2. The package is absolutely free for academic users. They can distribute it. For commercial purpose, they must contact with the author.
   3. The package can be used to analyse various compositions of a protein sequence.
   4. There is no limitation on size of the protein sequence.

Following things can be computed by using  proteinAnalysis
   
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
The package can be download by right click and then 'Save link as..'

## Usage example
```python
# import the package
from proteinAnalysis import proteinAnalysis as pan

# take a protein sequence
seq = 'GAVLIUXGAA'

# create a object of the class and pass the seq
panObj = pan(seq)

# call methods to print the composition details of the seq
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




