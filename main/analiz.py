import requests
from .models import Kani

for i in range(2):
    response = requests.get('https://api.kanye.rest')

    a = response.json()
    x = a['quote']


    # количество согласных и гласных букв
    def kolSogGlas(x):
        vowels = 0
        consonants = 0
        for i in x:
            letter = i.lower()
            if letter == "a" or letter == "e" or \
                    letter == "i" or letter == "o" or \
                    letter == "u" or letter == "y":
                vowels += 1
            if letter == 'b' or letter == 'c' or letter == 'd' or \
                    letter == 'f' or letter == 'g' or letter == 'h' or \
                    letter == 'j' or letter == 'k' or letter == 'l' or \
                    letter == 'm' or letter == 'n' or letter == 'p' or \
                    letter == 'q' or letter == 'r' or letter == 's' or \
                    letter == 't' or letter == 'v' or letter == 'w' or \
                    letter == 'x' or letter == 'y' or letter == 'z':
                consonants += 1
        gsbukv = [f'гласнные {vowels} согласнные {consonants}']
        return gsbukv


    # Подсчитает общее количество повторений каждой буквы
    def kolPov(x):
        string = x
        s_string = set(string)
        summ = []
        povt = []
        for s_symbol in s_string:
            count = 0
            for symbol in string:
                if s_symbol == symbol:
                    count += 1
            summ.append([s_symbol, count])
        for item in summ:
            povt.append(item)
        return povt

        # Вытащит 3 самых длинных слова


    def dlslov(x):
        l = x.split()

        def sortD(l):
            return len(l)

        l.sort(key=sortD, reverse=True)

        if len(l) == 2:
            dslov = [f'самые длинные слова {l[0], l[1]}']
        if len(l) == 1:
            dslov = [f'самые длинные слова {l[0]}']
        else:
            dslov = [f'самые длинные слова {l[0], l[1], l[2]}']
        return dslov

        # Посчитает среднюю длину всех слов в цитатe


    def srdlina(x):
        slova = x.split()
        kslova = len(slova)
        bukv = len(x) - x.count(' ')
        c = bukv // kslova
        srdlin = [f'средняя длина слов {c}']
        return srdlin


    # Подсчитает общее количество букв
    def kolB(x):
        xr = len(x) - x.count(' ')
        kol = [f'количество букв {xr}']
        return kol


    kol = kolB(x)
    srdlin = srdlina(x)
    gsbukv = kolSogGlas(x)
    povt = kolPov(x)
    dslov = dlslov(x)

    vse = [kol, srdlin, gsbukv, povt, dslov, ]

    form = Kani(content=x, razbor=vse)
    form.save()