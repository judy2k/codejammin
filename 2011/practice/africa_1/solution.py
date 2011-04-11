#!python
# -*- coding: utf-8 -*-

import logging
import optparse
import sys
import time


class Case(object):
	def __init__(self, case_num, fin, fout):
		self.case_num = case_num
		self.fin = fin
		self.fout = fout
	
	def run_case(self):
		start_time = time.time()
		self.read_case()
		self.solve_case()
		self._write_case_prefix()
		self.write_case()
		duration = time.time() - start_time
		logging.debug('Time for case %d: %.2fs', self.case_num, duration)
	
	def skip_case(self):
		self.read_case()
	
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
	def run(cls, fin, fout, selected_cases=None):
		case_count = int(fin.readline())
		
		start_time = time.time()
		if selected_cases is not None:
			executed_count = 0
			for case_index in range(case_count):
				case = cls(case_index + 1, fin, fout)
				if case_index+1 in selected_cases:
					case.run_case()
					executed_count += 1
				else:
					case.skip_case()
		else:
			for case_index in range(case_count):
				case = cls(case_index + 1, fin, fout).run_case()
			executed_count = case_count
		duration = time.time() - start_time
		logging.debug('Total Duration: %.2fs', duration)
		logging.debug('Average Case Time: %.5fs (%d cases executed)', duration/executed_count, executed_count)
		
		
def main(cls, argv=sys.argv[1:]):
	opar = optparse.OptionParser()
	opar.add_option('-v', '--verbose', action='count', default=0)
	opar.add_option('-s', '--select', action='append', default=None)
	options, args = opar.parse_args(argv)
	
	level = logging.INFO if options.verbose == 0 else logging.DEBUG
	logging.basicConfig(level=level, format="%(levelname)s: %(message)s")
	
	if options.select is None:
		if not 1 <= len(args) <= 2:
			opar.error('Input file must be specified.')
		fin = open(argv[0], 'r')
		fout = open(argv[1], 'w') if len(args) > 1 else sys.stdout
		cls.run(fin, fout)
	else:
		if len(args) != 1:
			opar.error('Only input file must be supplied when using --select')
		fin = open(argv[0], 'r')
		selected_cases = [int(i) for i in options.select]
		cls.run(fin, sys.stdout, selected_cases)