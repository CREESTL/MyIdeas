o=0
for i in range(0,5): #можно создать цикл без списка от 0 до 5 в данном случае

    x=int(input('Введите количество осадков за день: '))
    o+=x
print("Всего выпало "+str(o)+" миллиметров осадков.")