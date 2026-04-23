class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        for x in s:
            if x == '(' or x == '[' or x == '{':
                arr.append(x)
            elif len(arr) > 0:
                if x == ')':
                    if arr[-1] == '(':
                        arr = arr[:-1]
                    else:
                        return False
                elif x == ']':
                    if len(arr)>0 and arr[-1] == '[':
                        arr = arr[:-1]
                    else:
                        return False
                elif x == '}':
                    if arr[-1] == '{':
                        arr = arr[:-1]
                    else:
                        return False
            else:
                return False

        if len(arr) == 0:
            return True
        return False