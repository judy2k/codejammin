#!python
# -*- coding: utf-8 -*-

import logging
import optparse
import sys


class Case(object):
	def __init__(self, case_num, fin, fout):
		self.case_num = case_num
		self.fin = fin
		self.fout = fout
		self.read_case()
		self.solve_case()
		self._write_case_prefix()
		self.write_case()
		
	def read_case(self):
		raise NotImplementedError()
	
	def solve_case(self):
		raise NotImplementedError()
	
	def write_case(self):
		raise NotImplementedError()
	
	def read_float(self):
		return float(self.fin.readline())
		
	def read_float_list(self, ):
		return [float(p) for p in self.fin.readline().split(' ')]	
	
	def read_int(self):
		return int(self.fin.readline())
	
	def read_int_list(self, ):
		return [int(p) for p in self.fin.readline().split(' ')]

	def _write_case_prefix(self):
		print >>self.fout, 'Case #{0}:'.format(self.case_num),
		
	def write_int_list(self, i_list):
		print >>self.fout, ' '.join([str(i) for i in i_list])
	
	@classmethod
	def run(cls, fin, fout):
		case_count = int(fin.readline())
		for case_index in range(case_count):
			case = cls(case_index + 1, fin, fout)

			
class Africa1A(Case):
	def read_case(self):
		self.c = self.read_int()
		self.i = self.read_int()
		self.p_list = self.read_int_list()
	
	def solve_case(self):
		p_len = len(self.p_list)
		
		indexes = zip(range(p_len), self.p_list)
		indexes.sort(key=lambda x: x[1])
		
		self.p_list = [i[1] for i in indexes]
		
		for i in range(p_len):
			val1 = self.p_list[i]
			for j in range(i+1, p_len):
				res = val1 + self.p_list[j]
				if res > self.c:
					break
				elif res == self.c:
					self.result = sorted([indexes[i][0]+1, indexes[j][0]+1])
					return
		raise Exception()
	
	def write_case(self):
		self.write_int_list(self.result)


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
	
	Africa1A.run(fin, fout)


if __name__ == '__main__':
	main()