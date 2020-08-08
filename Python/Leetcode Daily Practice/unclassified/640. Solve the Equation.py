def dfafd(equation):
    parts = equation.split("=")
    left_part = parts[0]
    right_part = parts[1]
def evaluate(exp):
    tokens = exp.split("(?=[+-])")

    for token in tokens: