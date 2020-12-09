from collections import deque


class ParenthesesString:
  def __init__(self, str, openCount, closeCount):
    self.str = str
    self.openCount = openCount
    self.closeCount = closeCount

def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString('(',1,0))
    while queue:
        ps:ParenthesesString = queue.popleft()
        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.str)
        else:
            if ps.openCount < num :
                queue.append(ParenthesesString(ps.str+'(',ps.openCount+1, ps.closeCount))
            if ps.openCount > ps.closeCount:
                queue.append(ParenthesesString(ps.str+')', ps.openCount, ps.closeCount+1))
    return result

print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses(3)))
