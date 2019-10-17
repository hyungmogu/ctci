# Letter Case Permutation
#
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
# Note:
#
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# ============================================

class Solution:
    def letterCasePermutation(self, S):
        output = []
        temp_arr = [x for x in S.strip()]

        if len(temp_arr) == 0:
            return [""]

        self.letter_case_permutation_helper(temp_arr, 0, output)

        return output

    def letter_case_permutation_helper(self, temp_arr, idx, output):
        if idx >= len(temp_arr):
            output.append("".join(temp_arr))
            return

        if temp_arr[idx].isalpha():
            temp_arr_lower = temp_arr[:]
            temp_arr_upper = temp_arr[:]

            temp_arr_lower[idx] = temp_arr_lower[idx].lower()
            temp_arr_upper[idx] = temp_arr_upper[idx].upper()

            self.letter_case_permutation_helper(temp_arr_lower, idx+1, output)
            self.letter_case_permutation_helper(temp_arr_upper, idx+1, output)
        else:
            self.letter_case_permutation_helper(temp_arr, idx+1, output)

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCasePermutation("12345"))