"""Solution for http://www.checkio.org/mission/digit-stack/ in Python 2.7"""

def digit_stack(commands):
    result = 0
    stack = []
    for command in commands:
        words = command.split(" ")
        if words[0] == "PUSH":
            stack.append(int(words[1]))
        elif words[0] == "POP":
            if len(stack) > 0:
                result += stack.pop()
        elif words[0] == "PEEK":
            if len(stack) > 0:
                result += stack[-1]
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
