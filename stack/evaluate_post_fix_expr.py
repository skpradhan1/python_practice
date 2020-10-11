from stack.Stack import MyStack


def evaluate_post_fix(exp):
    stack = MyStack()
    try:
        for c in exp:
            if c.isdigit():
                stack.push(c)
            else:
                right = stack.pop()
                left = stack.pop()
                result = str(eval(left + c + right))
                stack.push(result)

        return stack.pop()
    except TypeError:
        return 'invalid sequence'


print("Result: " + str(evaluate_post_fix("921*-8-4+")))
print("Result: " + str(evaluate_post_fix("921*-8--4+")))