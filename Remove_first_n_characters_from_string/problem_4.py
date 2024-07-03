# solution 1
def remove_chars(txt, n):
    if n > len(txt):
        return ""
    else:
        return txt[n:]


txt = input()
n = int(input())
print(remove_chars(txt, n))


# solution 2
def remove_chars(txt, n):
    return txt[n:] #n: means the index of the string


txt = input()
n = eval(input())