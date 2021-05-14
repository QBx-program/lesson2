#ДЗ2

#Задание 1 Выяснить тип

type_print = [15 * 3, 15 / 3, 15 // 2, 15 **2]
for i in type_print:
    print(type(i))

#Задание 2-3 Работа со списком
text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+7', 'градусов']

for n, char_s in enumerate(text):
    text[n] = lambda p: f'"0{p}"' if p.isdigit() and len(p) == 1 else f'"{p}"' if p.isdigit() and len(p) > 1 else f'"{p[0]}0{p[1:]}"' if p[0] == '+' else p
    text[n] = text[n](char_s)
print(" ".join(text))

#Задание 4
works = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i, n in enumerate(works):
    print(f'Привет, {list(reversed(list(works[i].split(" "))))[0].capitalize()}')
a = 97.2

#Задание 5 со звездочками

def format_price(price):
    text_price = ''
    text_max = []
    for i, pr in enumerate(price):
        price_t = lambda b: '00' if int(b[0]) == 0 else f'0{b[0]}' if int(b[0]) < 10 and int(b[0]) != 0 else b[0]
        rub = str(int(pr) // 1)
        cop = price_t(str(round(float(pr) * 10 % 10, 2) * 10).split('.'))
        text_price = text_price + '{0}руб.{1}коп., '.format(rub, cop)
        text_max.append([f'{rub}руб.', f'{cop}коп.'])
    return text_price, text_max

price = [57.8, 46.51, 97, 77.0, 53.02, 68.01, 91.5]
print(format_price(price)[0])
print(format_price(sorted(price))[0])
price_new = price.copy()
print(format_price((reversed(sorted(price_new))))[0])
mp = list(max_price for i, max_price in enumerate(reversed(format_price(reversed(sorted(price_new)))[1][1:6])))
print(*[f'{f[0]}{f[1]},' for s, f in enumerate([r for r in mp])])







