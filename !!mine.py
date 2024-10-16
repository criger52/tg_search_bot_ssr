# def damerau_levenshtein_distance(s1, s2):
#     d = {}
#     lenstr1 = len(s1)
#     lenstr2 = len(s2)
#     for i in range(-1, lenstr1 + 1):
#         d[(i, -1)] = i + 1
#     for j in range(-1, lenstr2 + 1):
#         d[(-1, j)] = j + 1
#
#     for i in range(lenstr1):
#         for j in range(lenstr2):
#             if s1[i] == s2[j]:
#                 cost = 0
#             else:
#                 cost = 1
#             d[(i, j)] = min(
#                 d[(i - 1, j)] + 1,  # deletion
#                 d[(i, j - 1)] + 1,  # insertion
#                 d[(i - 1, j - 1)] + cost,  # substitution
#             )
#             if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
#                 d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + 1)  # transposition
#
#     return d[lenstr1 - 1, lenstr2 - 1]
#
#
# # def naive_string_matcher(string: str, sub_string: str):
# #     len_str = len(string)
# #     len_sub_str = len(sub_string)
# #     ans = []
# #     for i in range(len_str - len_sub_str + 1):
# #         if string[i:i + m] == sub_string:
# #             ans.append(i)
# #     return ans
#
# #mine
# def naive_search(string:str,sub_string:str):
#     #суффикс всегда включает первый символ и в последующие просто добавляются +1 елемент Не включает в себя последний элемент
#     #префикс всегда включает в себя последний символ и все возможные вариации комбинаций букв не включая первую
#     p = [0] * len(sub_string)
#     #p = []
#     j = 0
#     i = 1
#     while i < len(sub_string):
#         if sub_string[j] == sub_string[i]:
#             p[i] = j + 1
#             i += 1
#             j += 1
#         else:
#             if j == 0:
#                 p[i] = 0
#                 i += 1
#             else:
#                 j = p[j - 1]
#     #print(p)
#     len_sub_string = len(sub_string)
#     len_string = len(string)
#     i = 0
#     j = 0
#     while i < len_string:
#         if sub_string[i] == sub_string[j]:
#             i += 1
#             j += 1
#             if j == len_sub_string:
#                 print("образ найден1")
#                 break
#         else:
#             if j > 0:
#                 j = p[j - 1]
#             else:
#                 i += 1
#
#     if i == len_string and j != len_sub_string:
#         print("образ не найден2")
#
#
#
#     def distance(a, b):
#         "Calculates the Levenshtein distance between a and b."
#         n, m = len(a), len(b)
#         if n > m:
#             # Make sure n <= m, to use O(min(n,m)) space
#             a, b = b, a
#             n, m = m, n
#
#         current_row = range(n + 1)  # Keep current and previous row, not entire matrix
#         for i in range(1, m + 1):
#             previous_row, current_row = current_row, [i] + [0] * n
#             for j in range(1, n + 1):
#                 add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
#                 if a[j - 1] != b[i - 1]:
#                     change += 1
#                 current_row[j] = min(add, delete, change)
#
#         return current_row[n]
#     # def levenshtein_distance_algorithm(word1: str, word2: str):
#     #     # Каков путь замены word1 на word2. Сколько нужно итераций
#     #     # matrix = [[0]* (len(word1) + 1)] * (len(word2) + 1)# почему тут не может заполнить нормально?
#     #     matrix = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
#     #
#     #     for i in range((len(word2) + 1)):
#     #         # print(i)
#     #         matrix[i][0] = i
#     #     for i in range((len(word1) + 1)):
#     #         # print(i)
#     #         matrix[0][i] = i
#     #
#     #     for i in range(1, (len(word2) + 1)):
#     #         for j in range(1, (len(word1) + 1)):
#     #             if word1[j - 1] == word2[i - 1]:
#     #                 matrix[i][j] = matrix[i - 1][j - 1]
#     #             else:
#     #                 matrix[i][j] = min({matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]}) + 1
#     #
#     #     # for i in matrix:
#     #     #     print(i)
#     #
#     #     return matrix[-1][-1]


import hunspell

# Инициализация объектов Hunspell для русского и английского языков
h_en = hunspell.HunSpell('en_US.dic', 'en_US.aff')
h_ru = hunspell.HunSpell('ru_RU.dic', 'ru_RU.aff')


def correct_word(word):
    # Сначала пробуем английский словарь
    if not h_en.spell(word):  # Если слово содержит ошибку
        suggestions_en = h_en.suggest(word)
        if suggestions_en:
            return suggestions_en[0]  # Исправляем с помощью английского словаря

    # Если английский не нашел, пробуем русский словарь
    if not h_ru.spell(word):
        suggestions_ru = h_ru.suggest(word)
        if suggestions_ru:
            return suggestions_ru[0]  # Исправляем с помощью русского словаря

    # Если оба словаря считают слово правильным или нет предложений, возвращаем исходное слово
    return word


def correct_text(text):
    words = text.split()  # Разделяем текст по пробелам на слова
    corrected_words = []

    for word in words:
        corrected_word = correct_word(word)  # Исправляем слово
        corrected_words.append(corrected_word)

    # Восстанавливаем текст с исправленными словами
    corrected_text = ' '.join(corrected_words)
    return corrected_text


# Пример текста
text = "Превет world! This is an еxample тектс."

# Исправляем текст
corrected_text = correct_text(text)
print(corrected_text)







def corrected_text(string:str,sub_string:str):
    #print(string)
    #print(string.split('.'))
    #print(sub_string.split())
    ls = []
    sub_string_split = sub_string.split()
    string_split_sentences = string.split('.')


         #for j in range(len()): # чо? крч для того что бы смотреть все слова в подстроке на ошибки

                # крч надо проверять в каждом предложении циклом каждое слово на то похоже ли оно на то слово что нужно найти то есть алгорит лев дает короткий путь


    return ls

def find_occurrences(text:str, pattern:str):
    def compute_prefix_function(pattern):
        m = len(pattern)
        prefix = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix[j-1]
            if pattern[j] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix

    def kmp_search(txt:str, patern:str):
        n = len(text)
        m = len(pattern)
        prefix = compute_prefix_function(pattern)
        j = 0
        results = []
        for i in range(n):
            while j > 0 and text[i] != pattern[j]:
                j = prefix[j-1]
            if text[i] == pattern[j]:
                j += 1
            if j == m:
                results.append(i - m + 1)
                j = prefix[j-1]
        return results

    indices = kmp_search(text, pattern)
    sentences = text.split('.')
    result_sentences = []

    for index in indices:
        for sentence in sentences:
            if pattern in sentence and sentence not in result_sentences:
                result_sentences.append(sentence)
                break

    return result_sentences

