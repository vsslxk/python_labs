import sys
sys.stdin.reconfigure(encoding='utf-8')

from src.lib.text import normalize, tokenize, count_freq, top_n

'''
Меняет кодировку на utf-8 для корректной работы с входными данными через sys.stdin.reconfigure(encoding='utf-8')
Получает данные через sys.stdin.read() - текст
Возвращает общее количество слов в введенном тексте, количество уникальных слов;
и Топ-5 наиболее частых слов (при константе excel == True: красивый табличный вывод / excel == False: базовый вывод)
'''

excel = True

text = sys.stdin.read()
text = normalize(text)
tokens = tokenize(text)

print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(set(tokens))}')
print('Топ-5:')

if not excel:
    top = top_n(count_freq(tokens))
    for word, freq in top:
        print(f'{word}:{freq}')

if excel:
    top = top_n(count_freq(tokens))
    max_len = max(max([len(word[0]) for word in top])+1, 6)
    
    first_row = 'слово' + (max_len-5)*' ' + '|' +'  частота'
    print(first_row)
    print('-'*len(first_row))
    for word, freq in top:
            print(word + (max_len-len(word))*' ' + '| ' + str(freq))
    print('...')

