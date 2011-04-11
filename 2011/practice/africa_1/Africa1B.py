import solution

class Africa1B(solution.Case):
	def read_case(self):
		self.line = self.fin.readline().strip()
	
	def solve_case(self):
		self.result = ' '.join(reversed(self.line.split(' ')))
	
	def write_case(self):
		print >>self.fout, self.result


if __name__ == '__main__':
	solution.main(Africa1B)