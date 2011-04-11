import sys
sys.path[0:0] = ['..']

import solution


class Africa1A(solution.Case):
    def read_case(self):
        c = self.read_int()
        i = self.read_int()
        p_list = self.read_int_list()
        return c, i, p_list
    
    def solve_case(self, c, i, p_list):
        p_len = len(p_list)
        
        indexes, p_list = zip(
                *sorted(
                        zip(range(1, p_len+1), p_list),
                        key=lambda x: x[1]))
        
        for i in range(p_len):
            val1 = p_list[i]
            for j in range(i+1, p_len):
                res = val1 + p_list[j]
                if res > c:
                    break
                elif res == c:
                    return sorted([indexes[i], indexes[j]])
        raise Exception()
    
    def write_case(self, result):
        self.write_int_list(result)


if __name__ == '__main__':
    solution.main(Africa1A)