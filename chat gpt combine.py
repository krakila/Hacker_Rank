def merge_the_tools(s, k):
    for i in range(0, len(s), k):     # идём по строке с шагом k
        substring = s[i:i+k]          # берём подстроку длины k
        seen = set()                  # множество для отслеживания уже добавленных символов
        result = ''                   # результирующая строка
        for char in substring:       # проходим по символам подстроки
            if char not in seen:     # если символ ещё не был добавлен
                seen.add(char)       # добавляем в множество
                result += char       # и к результату
        print(result)                # печатаем результат


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)