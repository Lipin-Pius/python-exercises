#! /usr/bin/python
from sys import argv

if len(argv)==4: #to ensure that the command line parameter have exactly 4 elements including filename, operation and operands
	if argv[1]=="--add": # for addition operation
		print int(argv[2])+int(argv[3]) # operands read from commandline will be of type string convert them to int
						# perform addition operation and print the result
	elif argv[1]=="--sub":
		print int(argv[2])-int(argv[3]) # perform subtraction operation
	elif argv[1]=="--mul":
	        print int(argv[2])*int(argv[3]) # perform multiplication operation
	elif argv[1]=="--div":
        	print int(argv[2])/int(argv[3]) # perform division operation

