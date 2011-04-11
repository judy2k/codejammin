import solution


class Africa1A(solution.Case):
	def read_case(self):
		self.c = self.read_int()
		self.i = self.read_int()
		self.p_list = self.read_int_list()
	
	def solve_case(self):
		p_len = len(self.p_list)
		
		indexes = zip(range(1, p_len+1), self.p_list)
		indexes.sort(key=lambda x: x[1])
		
		indexes, self.p_list = zip(*indexes)
		
		for i in range(p_len):
			val1 = self.p_list[i]
			for j in range(i+1, p_len):
				res = val1 + self.p_list[j]
				if res > self.c:
					break
				elif res == self.c:
					self.result = sorted([indexes[i], indexes[j]])
					return
		raise Exception()
	
	def write_case(self):
		self.write_int_list(self.result)


if __name__ == '__main__':
	solution.main(Africa1A)