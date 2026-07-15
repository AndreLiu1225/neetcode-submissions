class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()

                if token == "+":
                    stack.append(first_operand + second_operand)
                elif token == "-":
                    stack.append(first_operand - second_operand)
                elif token == "*":
                    stack.append(first_operand * second_operand)
                elif token == "/":
                    stack.append(int(first_operand / second_operand))
        
        return stack[-1]
