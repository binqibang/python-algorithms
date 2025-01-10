def decode_string(s: str) -> str:
    # 3[a2[c]] -> accaccacc
    stack = []
    for ch in s:
        if ch != ']':
            stack.append(ch)
        else:
            curr_str = []
            while len(stack) > 0 and stack[-1].isalpha():
                curr_str.append(stack.pop())
            curr_str.reverse()
            stack.pop()
            curr_num = []
            while len(stack) > 0 and stack[-1].isdigit():
                curr_num.append(stack.pop())
            curr_num.reverse()
            repeat_times = int("".join(curr_num))
            for i in range(repeat_times):
                for c in curr_str:
                    stack.append(c)
    return "".join(stack)


if __name__ == '__main__':
    print(decode_string("3[a2[c]]"))
    print(decode_string("10[leetcode]"))
