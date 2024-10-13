# Каков путь замены word1 на word2. Сколько нужно итераций

def levenshtein_distance_algorithm(word1:str,word2:str):
    # matrix = [[0]* (len(word1) + 1)] * (len(word2) + 1)# почему тут не может заполнить нормально?
    matrix = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

    for i in range((len(word2) + 1)):
        # print(i)
        matrix[i][0] = i
    for i in range((len(word1) + 1)):
        # print(i)
        matrix[0][i] = i

    for i in range(1, (len(word2) + 1)):
        for j in range(1, (len(word1) + 1)):
            if word1[j - 1] == word2[i - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min({matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]}) + 1

    # for i in matrix:
    #     print(i)


    return matrix[-1][-1]

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




