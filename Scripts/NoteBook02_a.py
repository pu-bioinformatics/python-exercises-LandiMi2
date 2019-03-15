#! /home/cofia/miniconda3/bin/python

# Question - Calculate the % GC and % AT content in the trna sequence

#input as trna 


trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'

#Count C,G and total DNA 

no_C = trna.count ('c')

no_G = trna.count ('G')

dna_length = len(trna) 

# calculate percentage of GC contents in a sequence 

gc_percent = (no_G + no_C ) / dna_length * 100 

#Print out the percentage 
print ("Here is the GC percent of dna_seq:%.3f" %gc_percent)  






