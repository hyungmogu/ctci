# 51. N-Queens
#
#
# The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

class Solution:
    def solveNQueens(self, n):
        self.chessboard = [['.' for x in range(n)] for y in range(n)]
        self.output = []

        if n == 0:
            return []

        if self.solveNQueensHelper(0,n):
            return self.output[::-1]
        else:
            return []

    def solveNQueensHelper(self, idx_column, n):
        # 1. backtracking function
        #   - terminating case
            if idx_column == n:
                self.output.append(["".join(x) for x in self.chessboard])
                return True

        #   - recursive case
            for idx_row in range(n):
                self.chessboard[idx_row][idx_column] = 'Q'

                if not self.placement_is_valid(idx_column, idx_row, n):
                    self.chessboard[idx_row][idx_column] = '.'
                    continue

                self.solveNQueensHelper(idx_column + 1, n)
                self.chessboard[idx_row][idx_column] = '.'

            if len(self.output) > 0:
                return True
            else:
                return False

    def placement_is_valid(self, idx_column, idx_row, n):
        if (self.valid_placement_horizontal(idx_column, idx_row, n) and
            self.valid_placement_vertical(idx_column, idx_row, n) and
            self.valid_placement_trbl_diagonal(idx_column, idx_row, n) and
            self.valid_placement_tlbr_diagonal(idx_column, idx_row, n)):
            return True
        return False

    def valid_placement_horizontal(self, idx_column, idx_row, n):
        for j in range(n):
            if self.chessboard[j][idx_column] == 'Q' and (j != idx_row):
                return False
        return True

    def valid_placement_vertical(self, idx_column, idx_row, n):
        for i in range(n):
            if self.chessboard[idx_row][i] == 'Q' and (i != idx_column):
                return False
        return True

    def valid_placement_tlbr_diagonal(self, idx_column, idx_row, n):
        i = idx_column
        j = idx_row

        while i < n and j < n:
            if self.chessboard[j][i] == 'Q' and (i != idx_column and j != idx_row):
                return False

            i += 1
            j += 1

        i = idx_column
        j = idx_row

        while i >= 0 and j >= 0:
            if self.chessboard[j][i] == 'Q' and (i != idx_column and j != idx_row):
                return False

            i -= 1
            j -= 1

        return True

    def valid_placement_trbl_diagonal(self, idx_column, idx_row, n):
        i = idx_column
        j = idx_row

        while i >= 0 and j < n:
            if self.chessboard[j][i] == 'Q' and (i != idx_column and j != idx_row):
                return False

            i -= 1
            j += 1

        i = idx_column
        j = idx_row

        while i < n and j >= 0:
            if self.chessboard[j][i] == 'Q' and (i != idx_column and j != idx_row):
                return False

            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(3))