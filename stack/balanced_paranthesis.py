from stack.Stack import MyStack

def is_balanced(exp):
    s = MyStack()

    for char in exp:
        if char in ['{', '(', '[']:
            s.push(char)
        else:
            char1 = s.pop()
            if char == ']' and char1 != '[':
                return False
            if char == '}' and char1 != '{':
                return False
            if char == ')' and char1 != '(':
                return False
    if s.is_empty() is False:
        return False
    return True


input_string = "{[([({))]}}" #balanced string
print(input_string + " " + str(is_balanced(input_string)))