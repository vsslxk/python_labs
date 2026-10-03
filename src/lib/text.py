import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    Функция нормализует введенные текстовые данные
    Принимает на вход текстовые данные, две булевых переменных:
        casefold: True - приводит к casefold / False - использует lower()
        yo2e: True - заменяет Ё(ё) на Е(е) / False - оставляет Ё(ё)
    Возвращает текст приведенный к необходимому формату
    '''
    if casefold: text = text.casefold()
    else: text = text.lower()
    if yo2e: text = text.replace('ё', 'е')
    text = ' '.join(text.split())
    return text

def tokenize(text: str) -> list[str]:
    '''
    Функция разбивает введенный текст по небуквенно-цифровым разделителям
    Принимает на вход текстовые данные
    Возвращает список со словами(последовательностями символов \w + [-] в сложных словах
    '''
    our_alphas = re.finditer(r'\w+(-\w+)*', text)
    words = []
    for alphas in our_alphas:
        words.append(alphas.group())
    return words

def count_freq(tokens: list[str]) -> dict[str, int]:
    '''
    Функция считает частоты введенных значений в списке
    Принимает список с текстовыми элементами
    Возвращает словарь типа: {'елемент': частота появлений в списке}
    '''
    freq = dict()
    for element in tokens:
        if element not in freq: freq[element] = 1
        else: freq[element] += 1
    return dict(sorted(freq.items()))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''
    Функция возвращает топ-N по убыванию частоты; при равенстве — по алфавиту слова
    Принимает словарь с элементами и их частотами, число N - количество возвращаемых ТОП-элементов
    Возвращает отсортрованный список ТОП-N элементов с кортежами
    '''
    freqs = sorted(freq.items(), key = lambda x: (-x[1], x[0]))[:n]
    return freqs
