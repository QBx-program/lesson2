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

