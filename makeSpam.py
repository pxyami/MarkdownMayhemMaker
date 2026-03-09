import random

def make_spam_string(string, breaklineThreshold, breaklineSensitivity, maxRow, usage = "General"):
    stringToBeRepeated = list(reversed(string))
    markupPrefix = []
    breaklineThreshold = breaklineThreshold
    breaklineSensitivity = breaklineSensitivity
    maxRow = maxRow

    if usage == "General":
        markupPrefix = ["", "# ", "## ", "### "]

    elif usage == "Discord":
        markupPrefix = ["-# ", "", "# ", "## ", "### "]


    result_list = []
    for i in range(maxRow):
        r = random.randrange(0, len(markupPrefix))
        string = markupPrefix[r]

        count = 0
        while True:
            count += 1
            temp = stringToBeRepeated.pop()
            string += temp
            stringToBeRepeated = [temp,] + stringToBeRepeated

            r = random.random()
            if r < breaklineSensitivity or count >= breaklineThreshold:
                result_list.append(string)
                break

    # 출력 방식 1: 콘솔 출력만 가능
    # for row in result_list:
    #     print(row)


    # 출력 방식 2: 문자열로 출력
    result_string = ''
    for string in result_list:
        result_string = result_string + string
        result_string = result_string + '\n'
    return result_string
