#!python
# -*- coding: utf-8 -*-

import logging
import optparse
import sys

class Case(object):
	def __init__(num, fin, fout):
		self.read_case(fin)
		self.solve_case()
		self.write_case(num, fout)
		
	def read_case(self, fin):
		pass
	
	def write_case(self, fout):
		pass


def run(fin, fout):
	counter = 1
	while True:
		case = Case(counter += 1, fin, fout)
	
	
def main(argv=sys.argv[1:]):
	opar = optparse.OptionParser()
	opar.add_option('-v', '--verbose', action='count', default=0)
	
	options, args = opar.parse_args(argv)
	
	level = logging.INFO if options.verbose == 0 else logging.DEBUG
	logging.basicConfig(level=level)
	
	if len(args) != 2:
		opar.error('Input and output files must be specified.')
	
	fin = open(argv[0], 'r')
	fout = open(argv[1], 'w')
	
	run(fin, fout)

if __name__ == '__main__':
	main()