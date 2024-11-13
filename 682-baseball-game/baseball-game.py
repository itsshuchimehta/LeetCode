class Solution:
    def calPoints(self, operations: List[str]) -> int:
        resultStack = []

        for o in operations:
            if o == "+":
                if resultStack:
                    newRecord = int(resultStack[-1]) + int(resultStack[-2])
                    resultStack.append(newRecord)
            elif o == "C":
                if resultStack:
                    resultStack.pop()
            elif o == "D":
                if resultStack:
                    newRecord = int(resultStack[-1]) * 2
                    resultStack.append(newRecord)
            else:
                resultStack.append(int(o))
        return sum(resultStack)