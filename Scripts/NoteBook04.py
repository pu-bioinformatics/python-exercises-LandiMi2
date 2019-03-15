#! /home/cofia/miniconda3/bin/python

# Question 1 - Using strings, lists, tuples and dictionaries concepts, find the reverse complement of AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA

#create a variable having a string called dna
dna = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
#convert a string to list
dna1= list(dna)
#Reverse the list
dna1.reverse()
#remove spaces in between the list 
reverse_strand = "".join(dna1)

#create a dictornary that defines how you can substitute each item in your list to make a complentary list 
dna_dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

#call out you dictionary and let it subsitute bases in the list as defined 
comp = [dna_dic[i] for i in reverse_strand]

complementary = "".join(comp) 

print("Here is the reverse strand of dna strans:%s " %reverse_strand)
print("Here is the reverse complementary strand of dna:%s" %complementary)

