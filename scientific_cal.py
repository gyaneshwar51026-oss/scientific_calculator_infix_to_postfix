
def infix_to_postfix(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3
    }

    right_associative = {'^'}
    stack = []
    output = []
    i = 0

    while i < len(expression):
        char = expression[i]

        # Ignore spaces
        if char.isspace():
            i += 1
            continue

        # Read numbers, including decimals
        if char.isdigit() or char == '.':
            number = char
            i += 1

            while i < len(expression) and (
                expression[i].isdigit() or expression[i] == '.'
            ):
                number += expression[i]
                i += 1

            output.append(number)
            continue

        # Opening bracket
        elif char == '(':
            stack.append(char)

        # Closing bracket
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            if not stack:
                raise ValueError("Mismatched parentheses")

            stack.pop()

        # Operators
        elif char in precedence:
            while (
                stack
                and stack[-1] != '('
                and (
                    precedence[stack[-1]] > precedence[char]
                    or (
                        precedence[stack[-1]] == precedence[char]
                        and char not in right_associative
                    )
                )
            ):
                output.append(stack.pop())

            stack.append(char)

        else:
            raise ValueError(f"Invalid character: {char}")

        i += 1

    # Pop remaining operators
    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses")

        output.append(stack.pop())

    return " ".join(output)


expression = input("Enter infix expression: ")

try:
    print("Postfix expression:", infix_to_postfix(expression))
except ValueError as error:
    print("Error:", error)
