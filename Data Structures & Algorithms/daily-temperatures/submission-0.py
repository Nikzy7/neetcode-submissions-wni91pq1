class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        answer = [0 for _ in temperatures]

        for t in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(t)
            elif temperatures[t] <= temperatures[stack[-1]]:
                stack.append(t)
            else:
                while stack:
                    if temperatures[stack[-1]] < temperatures[t]:
                        index = stack.pop()
                        answer[index] = t - index
                    else:
                        break
                stack.append(t)

        for s in stack:
            answer[s] = 0

        return answer
