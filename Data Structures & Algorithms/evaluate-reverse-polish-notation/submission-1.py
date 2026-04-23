class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def getnums():
            nonlocal stack
            n1 = int(stack[-1])
            stack.pop()
            n2 = int(stack[-1])
            stack.pop()
            return n1,n2

        for c in tokens:
            if c=='+':
                n1,n2 = getnums()
                stack.append(str(n2+n1))
            elif c=='-':
                n1,n2 = getnums()
                stack.append(str(n2-n1))
            elif c=='*':
                n1,n2 = getnums()
                stack.append(str(n2*n1))
            elif c=='/':
                n1,n2 = getnums()
                division = int(n2/n1)
                stack.append(str(division))
            else:
                stack.append(c)
            print(stack)

        return int(stack[-1])