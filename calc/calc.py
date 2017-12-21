#! /bin/python
import click

@click.command()
@click.option('--add', nargs=2, type=float)
@click.option('--sub', nargs=2, type=float)
@click.option('--mul', nargs=2, type=float)
@click.option('--div', nargs=2, type=float)
def calc(add,sub,mul,div):
	if add and not sub and not mul and not div: # if the option is only --add
		print (add[0]+add[1]) # printing the sum of two parameters
	elif sub and not add and not mul and not div:# if the option is only --sub
		print (sub[0]-sub[1])# printing the subtraction of two parameters
	elif mul and not add and not sub and not div:# if the option is only --mul
		print (mul[0]*mul[1])# printing the product of two parameters
	elif div and not add and not sub and not mul:# if the option is only --div
		print (div[0]/div[1])# printing the division of two parameters

