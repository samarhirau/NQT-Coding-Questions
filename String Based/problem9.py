# Replace character in string


def replace_character(s, old, new):

    result = ""

    for c in s:
        if c == old:
            result += new
        else:
            result += c
    return result


s = input().strip()
old = input().strip()
new = input().strip()
result = replace_character(s, old, new)
print(result)