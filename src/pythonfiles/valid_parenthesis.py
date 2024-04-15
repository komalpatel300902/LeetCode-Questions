class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        dic = {"}":"{",")":"(",']':"["}
        for x in s:
            length = len(lst)

            if (x == "}" or x == ")" or x == "]") and length == 0 :
                return False
            if x == "(" or x == "[" or x == "{":
                lst.append(x)
            elif (x == "}" or x == ")" or x == "]") and length != 0 :
                c = lst.pop(length-1)
                if c != dic[x] :
                    return False
        if len(lst) == 0:
            return True
        else:
            return False
        