with open('input.txt') as file:
    # чтение блока со словарём
    size = int(file.readline())
    dictionary = [file.readline().replace('\n', '').lower() for i in range(size)]
    print('INPUT DICTIONARY\n' + ' '.join(dictionary))

    # чтение текста для пооверки
    size = int(file.readline())
    text = file.read()
    print(f'\nINPUT TEXT:\n {text}')
    text = text.replace('\n', ' ').split()

    # поиск ошибок
    mistakes = tuple(filter(lambda word: word.lower() not in dictionary, text))

    # вывод ответа
    print('ANSWER:\n' + ' '.join(mistakes))
