print("Здравствуй.\nТебе предстоит пройти небольшой тест по физике. После прочтения задания выбери правильный ответ и "
      "введи букву, соответствующую ему в поле 'Ответ'(скобку после буквы указыват не надо).При наличии нескольких"
      " вариантов ответа, пиши их через запятую.")
print('\n№1'+'\nЧему равняется значение ускорения свободного падeния на Земле')
print('a)10 m/c^2'+'\nb)9.8 m/c^2'+'\nc)3.14 m/c^2'+'\nd)6.28 m/c^2')
mark=0
bill=0
ans=input('\nОтвет ')
if ans=='b':
    mark+=1
    bill+=1
else:
    mark+=0
    bill += 1
print('№2'+'\nНайти период вращения диска, который совершил 10 оборотов за 20с.')
print('a)2c'+'\nb)50c'+'\nc)5c'+'\nd)0.2c')
ans=input('\nОтвет ')
if ans=='a':
    mark+=1
    bill+=1
else:
    mark+=0
    bill += 1
print('№3'+'\nПловец плывёт по течению реки. Определите скорость пловца относительно берега реки,'
'если скорость пловца относительно воды 1,5 м/с, а скорость течения реки 0,5м/с.')
print('a)0.5m/c'+'\nb)1m/c'+'\nc)1.5m/c'+'\nd)2m/c')
ans=input('\nОтвет ')
if ans=='d':
    mark+=1
    bill += 1
else:
    mark+=0
    bill += 1
print('№4'+'\nНазовите виды деформации')
print('a)Сжатие'+'\nb)Перелом'+'\nc)Кручение'+'\nd)Изгиб')
ans=input('\nОтвет ')
if 'a' and 'c' and 'd' in ans:
    mark+=1
    bill += 1
else:
    mark+=0
    bill += 1
print('№5'+'\nМомент силы относительно точки считается положительным:')
print('\na)Если под действием силы тело поворачивается относительно центра моментов против часовой стрелки.' 
      '\nb)Eсли под действием силы тело поворачивается относительно центра моментов по часовой стрелки.'
      '\nc)Eсли тело стремится повернуться против часовой стрелки.'
      '\nd)Eсли тело стремится повернуться против часовой стрелки.')
ans=input('\nОтвет ')
if ans=='a':
    mark+=1
    bill += 1
else:
    mark+=0
    bill += 1
if bill==5:
    print("Твоя оценка за этот тест: ")
    if mark==1:
        print('1')
    elif mark==2:
        print('2')
    elif mark==3:
        print('3')
    elif mark==4:
        print('4')
    elif mark==5:
        print("5"+"\nОтличная работа!")
all_ans=input('\nЕсли ты хочешь узнать правильные ответы, напиши "Да". ')
if all_ans=='Да':
    print('Вот список правильных ответов: '
          '\n№1 b'
          '\n№2 а'
          '\n№3 d'
          '\n№4 a,c,d'
          '\n№5 а')
if all_ans=='Да':
    print('\nТест создал Егоров Данила,11Б класс.')
n = input()





