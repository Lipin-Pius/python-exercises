#!/bin/python

def permute():

    noofPerm = 1000001 #for millionth permutation for 0th permutation is 0123456789
    i = 1

    factoradic = [] # list t store the factoradic representation of noofPerm

    while noofPerm is not 0: 
	    factoradic.append(noofPerm%i)
	    noofPerm = noofPerm/i
	    i = i+1

# Calculating the Factoradic Representaion of noofPerm

    charlist = [0,1,2,3,4,5,6,7,8,9] # list to be permuted

    output = [] # to store the millionth permutation of charlist


    if len(charlist) > len(factoradic):
	    unused = len(charlist) - len(factoradic)
	    for i in range(0,unused):
	    	output.append(charlist.pop(0))
	    	charlist = [ charlist[j] for j in range(0,len(charlist)) ]

# to copy elements from charlist to output that need not be changed 


    while len(charlist) is not 0:
	    i = len(charlist)
	    i = factoradic[i-1]
	    output.append(charlist.pop(i))
	    charlist = [ charlist[j] for j in range(0,len(charlist)) ]

# changing and copying the charlist(0th permutation) to output(millionth) based on
# the factoradic repersentation


    str1 = ''.join(str(e) for e in output) # converting output list containing integer
# to string to print

    return  str1 # returning the output millionth perutation

if __name__=='__main__':
    result=permute()
    print result
