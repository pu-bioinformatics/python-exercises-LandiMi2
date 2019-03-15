#! /home/cofia/miniconda3/bin/python


#Question 1 - Given the following amino acid sequence (MNKMDLVADVAEKTDLSKAKATEVIDAVFA), find the first, last and the 5th amino acids in the sequence.

amino_acid = ("MNKMDLVADVAEKTDLSKAKATEVIDAVFA")
print ('Here is the last amino acid:', amino_acid[0])
print ('Here is the last amino acid:', amino_acid[-1])
print ('Here is the fifth amino acid:', amino_acid[4])


#Question 2 - he above amino acid is a bacterial restriction enzyme that recognizes "TCCGGA". Find the first restriction site in the following sequence: AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA

dna = ("AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA") 

restriction = 'TCCGGA'

print("The are %d restriction sites, the frist restriction site is on position %d to %d  " 
      % ( dna.count(restriction), dna.find(restriction), dna.find(restriction) + len(restriction)))