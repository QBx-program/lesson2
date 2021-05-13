#ДЗ2

#Задание 1 Выяснить тип

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

#Задание 2 Работа со списком

text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index_list = 0
for i in text:
    if i.isdigit():
        if len(i) < 2:
            text[index_list] = '"0' + i +'"'
        else:
            text[index_list] = '"' + i + '"'
    index_list += 1

print(" ".join(text))