#!/bin/python

import click

@click.command()
@click.option('--nand', nargs=2)
@click.option('--nor', nargs=2)

class Gate(object):
""" class representing a gate. It can be any gate. """
	def __init__(self, *args):
        """ initialise the class """
		self.input = args
		self.output = None

	def logic(self):
        """ the intelligence to be performed """
		raise NotImplementedError

	def output(self):
        """ the output of the gate """
		return self.output


class AndGate(Gate):
    """ class representing AND gate """

	def logic(self):
		self.output = self.input[0] and self.input[1]
		return self.output



class OrGate(Gate):
    """ class representing AND gate """
	def logic(self):
		self.output = self.input[0] or self.input[1]
		return self.output


class NotGate(Gate):
    """ class representing NOT gate """

	def logic(self):
		self.output = not self.input[0]
		return self.output


class NandGate(AndGate, NotGate):
   """ class representing NAND GATE """
	
	def logic(self):
		andResult = super(Nand, self).logic()
		NotGate.__init__(self, andResult)
		NotGate.logic(self)

class NorGate(OrGate, NotGate):
  """ class representing NOR GATE """
   
 
	def logic(self):
		orResult = super(OrGate, self).logic()
		NotGate.__init__(self, orResult)
		NotGate.logic(self)


def cli(nand, nor):
	if nand and not nor:
		nand = NandGate(nand)
		nand.logic()
		print(nand.output)
	elif nor and not nand:
		nor = NorGate(nor)
		nor.logic()
		print(nor.output)
			
			
			
