class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])

        seen = set()
        q = deque()

        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1) and board[i][j]=='O':
                    seen.add((i,j))
                    q.append((i,j))
                if (j==0 or j==n-1) and board[i][j]=='O':
                    seen.add((i,j))
                    q.append((i,j))

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for r_off, c_off in [[-1,0],[1,0],[0,-1],[0,1]]:
                    r_new, c_new = r+r_off, c+c_off
                    if 0<=r_new<m and 0<=c_new<n and board[r_new][c_new]=='O' and (r_new,c_new) not in seen:
                        q.append((r_new,c_new))
                        seen.add((r_new, c_new))

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and (i,j) not in seen:
                    board[i][j] = 'X'
        


        