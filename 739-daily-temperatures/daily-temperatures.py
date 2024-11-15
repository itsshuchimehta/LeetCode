class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((t, i))
            else:
                while stack and stack[-1][0] < t:
                    current = stack.pop()
                    answer[current[1]] = i - current[1]
                   
                stack.append((t,i))
        return answer
