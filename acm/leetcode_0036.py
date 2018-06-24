# -*- coding: utf-8 -*-

class Solution(object):
    def isDuplicated(self, lst):
        return len([x for x in lst if x != '.']) == len(set([x for x in lst if x != '.']))

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            if not self.isDuplicated(board[i]): return False

        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            #print col
            if not self.isDuplicated(col): return False

        for i in range(3):
            for j in range(3):
                col = []
                for k in range(3):
                    col += board[i * 3 + k][j * 3 : j * 3 + 3]
                #print col
                if not self.isDuplicated(col): return False

        return True
