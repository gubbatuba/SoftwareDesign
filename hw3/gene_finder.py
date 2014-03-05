# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Subhash Gubba

Took help from Deniz Celik and Ryan Louie on this one
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle
from load import load_seq
#dna = load_seq("./data/X73525.fa")

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    cuduns = []
    pro = []
    for i in range(len(dna)/3):
        cuduns.append(dna[:3])
        dna = dna[3:]
    		#Hmm, this is an interesting way to chunk your data. Its not bad though.

    for x in range(len(cuduns)):
        for i in codons:
            for j in i:
                if j == cuduns[x]:
                    pro.append(aa[codons.index(i)])
    return collapse(pro)
         
    # YOUR IMPLEMENTATION HERE


def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    a = coding_strand_to_AA('ATC')
    b = coding_strand_to_AA('TCTCATATCACA')
    a1 = 'I'
    b1 = 'SHIT'
    if a == a1:
        print 'good'
    else:
        print 'bad'
    
    if b == b1:
        print 'good'
    else:
        print 'bad'
            
coding_strand_to_AA_unit_tests()	#Any tests that you run should be in an if __main__
									#statement ideally and generally should be removed
									#before submitting your code
    # YOUR IMPLEMENTATION HERE

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """

    #This function is bugged!
    # On my unit tests, this function returns exactly the right sequence, but it always
    # adds a space at the end of the returned string, which screws up your later functions
    # get_all_ORFs_both_strands and longest_ORF (Its only counted once in grading though)

    dna2 = " "	#This is where the bug is coming from. If you are initilizing a string,
    			# start out with "" rather than " ". Otherwise you are adding a space
    			# to the beginning of the sequence, then reversing it to the end with
    			# your [::-1] code at the end
    for i in range(len(dna)):        
        if dna[i] == 'A':
            dna2 += 'T'
        elif dna[i] == 'T':
            dna2 += 'A'
        elif dna[i] == 'G':
            dna2 += 'C'
        elif dna[i] == 'C':
            dna2 += 'G'
        else:
            print "error"
    dna3 = dna2[::-1]	#Good use of this substringing, but you could also just
    					# "return dna2[::-1]" rather than initilize a new variable.
    					# Its mostly a matter of taste though.
    return dna3
    # YOUR IMPLEMENTATION HERE

def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    w = get_reverse_complement('AAATTTGGGCCC')
    v = get_reverse_complement('ATGCCGTA')
    print w
    print v
    # YOUR IMPLEMENTATION HERE    
get_reverse_complement_unit_tests()
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    
cidins = []
 stops = ['TAG','TAA','TGA']
    for i in range(((len(dna)/3)+1)):
        cidins.append(dna[:3])
        dna = dna[3:]
    if cidins[-1]!='TAG' or cidins[-1]!='TAA' or cidins[-1]!='TGA':
        cidins.append('TAG')
    for x in range(len(cidins)):
        for i in stops:
            if i == cidins[x]:
                return collapse(cidins[:x]) """
                
    frame = dna[:3]
    newdna = ''
    stop = codons[aa.index('|')]
    while frame != stop[0] and frame != stop[1] and frame != stop[2] and frame:
    						#Hmm, once again this is a creative solution not to use an
    						# iterator. It is quite elegantly compact. I will mention that
    						# you could save even a bit more space by having your while use
    						# the in keyword so it reads: "while frame and not frame in stop:"
        newdna += frame
        dna = dna[3:]
        frame = dna[:3]
        
    return newdna

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    c = rest_of_ORF('ATGGTATTTTAAGGG')
    d = rest_of_ORF('ATGGTATTTTGAGGG')
    e = rest_of_ORF('ATGGTATTTTAGGGG')
    f = rest_of_ORF('ATGTTTTAAGGG')
    
    if c == 'ATGGTATTT':
        print 'good'
    else:
        print 'bad'
    if d == 'ATGGTATTT':
        print 'good'
    else:
        print 'bad'
    if e == 'ATGGTATTT':
        print 'good'
    else:
        print 'bad'
    if f == 'ATGTTT':
        print 'good'
    else:
        print 'bad'
    # YOUR IMPLEMENTATION HERE
rest_of_ORF_unit_tests()
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    orfs = []
    
    
    """while len(dna)>=3 and dna[:3] != 'ATG':
        rORF = rest_of_ORF(dna)
        print rORF  
        orfs.append(rORF)
        dna = dna[len(rORF)+3:]
    """
    #Use your IDE to comment sections in python - don't use docstrings as block comments
    # because if you do they'll show up in a function's documentation. Its bad style


    #This function is bugged! Often, it is appending '' to the lists that you
    # are returning. This bug is cascading through the next two functions as well.

    while dna:
        while dna and dna[:3] != 'ATG':
            dna = dna[3:]
        orf = (rest_of_ORF(dna))	#I think the source of your bug is that if you iterate
        							#dna down in your while loop to '', it still gets passed
        							# to rest_of_ORF here and gets appended to your returned
        							# string
        orfs.append(orf)
        dna = dna[len(orf)+3:]
    return orfs
    
    #Nicely compact function
        
    """
    return ORFs
    """
    # ^ Why is this doctring here?
find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCCG")
    # YOUR IMPLEMENTATION HERE        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    
    # YOUR IMPLEMENTATION HERE
    

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ar = (find_all_ORFs_oneframe(dna))
    ar.extend(find_all_ORFs_oneframe(dna[1:]))
    ar.extend(find_all_ORFs_oneframe(dna[2:]))
    # YOUR IMPLEMENTATION HERE
    return ar
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    
    test = find_all_ORFs("ATGCATGAATGTAG")
    print test
        
    # YOUR IMPLEMENTATION HERE
find_all_ORFs_unit_tests()

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return find_all_ORFs(dna)+find_all_ORFs(get_reverse_complement(dna))

    	#Good. Nice one-liner
    
    # YOUR IMPLEMENTATION HERE
find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    # YOUR IMPLEMENTATION HERE
    return max(find_all_ORFs_both_strands(dna))
    	#Good use of max, but I believe you need to include a "key=len" argument in there
    	# this function is returning bugged because of the  all_ORFs_oneframe bug, but
    	# otherwise this might give you issues. Just keep it in mind for the future
    
    
def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    print longest_ORF("ATGCGAATGTAGCATCAAA")
    # YOUR IMPLEMENTATION HERE
longest_ORF_unit_tests()
def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
        
    dnl = list(dna)
    shuffled=[]
    for i in range(0,num_trials):
        shuffle(dnl)
        shuffled.append(len(longest_ORF(collapse(dnl))))
        #shuffled[i] = len(longest_ORF(collapse(dnl)))
    return max((shuffled))

    # YOUR IMPLEMENTATION HERE
print longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 50)

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    dnx = find_all_ORFs_both_strands(dna)
    dnx = [i for i in dnx if len(i)>threshold]
    dnx = [coding_strand_to_AA(i) for i in dnx]
    return dnx
        
    # YOUR IMPLEMENTATION HERE

#print gene_finder(dna,444)
