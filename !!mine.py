def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + 1)  # transposition

    return d[lenstr1 - 1, lenstr2 - 1]


# def naive_string_matcher(string: str, sub_string: str):
#     len_str = len(string)
#     len_sub_str = len(sub_string)
#     ans = []
#     for i in range(len_str - len_sub_str + 1):
#         if string[i:i + m] == sub_string:
#             ans.append(i)
#     return ans

#mine
def naive_search(string:str,sub_string:str):
    #суффикс всегда включает первый символ и в последующие просто добавляются +1 елемент Не включает в себя последний элемент
    #префикс всегда включает в себя последний символ и все возможные вариации комбинаций букв не включая первую
    p = [0] * len(sub_string)
    #p = []
    j = 0
    i = 1
    while i < len(sub_string):
        if sub_string[j] == sub_string[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    #print(p)
    len_sub_string = len(sub_string)
    len_string = len(string)
    i = 0
    j = 0
    while i < len_string:
        if sub_string[i] == sub_string[j]:
            i += 1
            j += 1
            if j == len_sub_string:
                print("образ найден1")
                break
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    if i == len_string and j != len_sub_string:
        print("образ не найден2")