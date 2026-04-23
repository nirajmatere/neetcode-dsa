class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [0] * 10
        col_check = [0] * 10
        box_check = [0] * 10

        # Row check
        for row in board:
            row_check = [0] * 10
            for num in row:
                if num != '.':
                    if row_check[int(num)] != 0:
                        return False
                    row_check[int(num)] = int(num)

        # Column Check
        col = 0
        while col < 9:
            col_check = [0] * 10
            row = 0
            while row < 9:
                if board[row][col] != '.':
                    if col_check[int(board[row][col])] != 0:
                        return False
                    col_check[int(board[row][col])] = int(board[row][col])
                row += 1
            col += 1
        
        # Box Check # My solution working but not readable.
        # col = 0
        # row = 0
        # counter = 1
        # while col < 9:
        #     while row < 9:
        #         if board[row][col] != '.':
        #             if box_check[int(board[row][col])] != 0:
        #                 return False
        #             box_check[int(board[row][col])] = int(board[row][col])
        #         row += 1
        #         if row % 3 == 0:
        #             break
        #     col += 1
        #     if col % 3 == 0:
        #         box_check = [0] * 10
        #     if counter <= 3:
        #         if counter == 1:
        #             row = 0
        #         elif counter == 2:
        #             row = 3
        #         elif counter == 3:
        #             row = 6
        #     if col == 9 and counter <= 3:
        #         col = 0
        #         counter += 1
        #         if counter == 4:
        #             break

        # Box Check: Chatgpt solution, working and readable
        for box_row in range(0, 9, 3):       # 0, 3, 6
            for box_col in range(0, 9, 3):   # 0, 3, 6
                box_check = [0] * 10
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row + i][box_col + j]
                        if cell != '.':
                            num = int(cell)
                            if box_check[num] != 0:
                                return False
                            box_check[num] = num

        return True

                



        
                