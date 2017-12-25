import click

@click.command()
@click.option('--nand', nargs=2)
@click.option('--nor', nargs=2)

class Gate(object):
	def __init__(self, *args):
		self.input = args
		self.output = None
	def logic(self):
		raise NotImplementedError
	def output(self):
		return self.output

class AndGate(Gate):
	def logic(self):
		self.output = self.input[0] and self.input[1]
		return self.output

class OrGate(Gate):
	def logic(self):
		self.output = self.input[0] or self.input[1]
		return self.output

class NotGate(Gate):
	def logic(self):
		self.output = not self.input[0]
		return self.ouput

class NandGate(AndGate, NotGate):
	def logic(self):
		andResult = super(NandGate, self).logic()
		NotGate.__init__(self, andResult)
		NotGate.logic(self)

class NorGate(OrGate, NotGate):
	def logic(self):
		orResult = super(NorGate, self).logic()
		NotGate.__init__(self, orResult)
		NotGate.logic(self)

def test(nand, nor):
	if nand and not nor
		nd = NandGate(nand)
		nd.logic()
		print(nd.output)
 	elif nor and not nand:
 		nr = NorGate(nor)
	 	nr.logic()
	 	print(nr.output)
