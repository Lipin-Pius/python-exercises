#!/usr/bin/python
# -*- coding: utf-8 -*-

import click



@click.command()
@click.option('--nand', nargs=2, type=bool)
@click.option('--nor', nargs=2, type=bool)
def gates(nand, nor):
    if nand and not nor:
        nAnd = NandGate(nand[0], nand[1]).logic()
        print(nAnd)
    elif nor and not nand:
        nOr = NorGate(nor).logic()
        print(nOr)


class Gate(object): #Bsoc functionalities of a logic ggate input logic and output

    def __init__(self, *args):
        self.input = args
        self.output = None

    def logic(self):
        raise NotImplementedError

    def output(self):
        return self.output


class AndGate(Gate): #simulation of And logic

    def logic(self):
        self.output = self.input[0] and self.input[1]
        return self.output


class OrGate(Gate): # simulation of Or Logic

    def logic(self):
        self.output = self.input[0] or self.input[1]
        return self.output


class NotGate(Gate): # simulation of Not logic

    def logic(self):
        self.output = not self.input[0]
        return self.output


class NandGate(AndGate, NotGate): # simulation of Nand Logic

    def logic(self):
        andResult = super(NandGate, self).logic()
        NotGate.__init__(self, andResult)
        self.output = NotGate.logic(self)
        return self.output



class NorGate(OrGate, NotGate): # Simulation of Nor Gate

    def logic(self):
        orResult = super(NorGate, self).logic()
        NotGate.__init__(self, orResult)
        self.output = NotGate.logic(self)
        return self.output



			
