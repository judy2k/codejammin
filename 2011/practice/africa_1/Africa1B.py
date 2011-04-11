import sys
sys.path[0:0] = ['..']

import solution

class Africa1B(solution.Case):
    def read_case(self):
        return self.fin.readline().strip(),
    
    def solve_case(self, line):
        return ' '.join(reversed(line.split(' ')))
    
    def write_case(self, result):
        print >>self.fout, result


if __name__ == '__main__':
    solution.main(Africa1B)