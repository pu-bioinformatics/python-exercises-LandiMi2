#! /home/cofia/miniconda3/bin/python

#Question - Write a function percentageGC that calculates the GC content of a DNA sequence
#         - The function should return the %GC content
#         - The Function should return a message if the provided sequence is not DNA (This should be checked by a different function, called by your function)


#input sequence data mydna, yourdna and testdna

mydna = "CAGTGATGATGACGAT"
yourdna = "ACGATCGAGACGTAGTA"
testdna = "ATFRACGATTGHAHYAK"

#create a function that returns the percentage GC content form mydna and yourdna sequence data 

def percent_GC(seq): ## Should firt test if the seqence is avalid DNA seq -2
    gc_count = seq.count('G') + seq.count('C')
    return 100 * (gc_count/len(seq))

#Define what makes a DNA strand
proper_DNA="ATGC"

#create a function that returns whether sequence data is a DNA data set 
def valid(sequence):
    for base in sequence: 
        if base not in proper_DNA: 
            return "This is Not DNA sequence" ##CK: This function should be called by the percent_GC -1
            # so the return should be True or False 
    return "This is DNA sequence"     
#creating a variable calling the function created to enable printing the results                
testdna1 = valid(testdna)
mydna1=percent_GC(mydna)
yourdna1=percent_GC(yourdna)

#print out results of percentage GC content and if sequence is DNA or not
    
print ('Here is the percentage GC content of mydna sequence:%.2f' %mydna1)
print ('Here is the percentage GC content of yourdna sequence sequence:%.2f' %yourdna1)
print ('Checking if testdna sequence is DNA: %s' %testdna1)


