# Generate Parenthesis
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        temp_str = ""
        total = n

        if n == 0:
            return []

        self.generate_parenthesis_helper("(",n-1,n,total,temp_str,output)

        return output

    def generate_parenthesis_helper(self,bracket,m,n,total,temp_str,output):
        temp_str += bracket

        if not self.is_valid(m,n,total):
            return False

        if self.terminating_condition_is_reached(m,n):
            output.append(temp_str)
            return False

        self.generate_parenthesis_helper("(",m-1,n,total,temp_str,output)
        self.generate_parenthesis_helper(")",m,n-1,total,temp_str,output)

    def is_valid(self,m,n,total):
        num_left_bracket = total - m
        num_right_bracket = total - n

        if m < 0 or n < 0:
            return False

        if num_right_bracket > num_left_bracket:
            return False

        return True

    def terminating_condition_is_reached(self,m,n):
        if m == 0 and n == 0:
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    n = 0
    print(solution.generateParenthesis(n))