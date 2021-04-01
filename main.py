#number 1 - переменные
print('Калькулятор. Ввидите два числа, для проведения арифмитических вычислений с ними')
A = int(input('Ввидите число A :'))
B = int(input('Ввидите число B :'))
plus = A + B
print('При сложении A и B вы получите: ', plus)
minus = A - B
print('При вычитании A и B вы получите: ', minus)
multiplication = A * B
print('При умножении A и B вы получите: ', multiplication)
division = A / B
division = float(division)
print('При делении A и B вы получите: ', division)
stepeni = A ** B
print('При возведении A в степень B вы получите: ', stepeni)

#number 2 - время
seconds = int(input('Введите кол-во секунд :'))
h = ((seconds//3600))%24
m = (seconds//60)%60
s = seconds%60
print( '{0}:{1:=02}:{2:=02}'.format(h, m, s) )

#number 3 - узнать число
num = int(input('Введите число'))
count = str(num)
count_1 = count + count
count_2 = count + count + count
summa = num + int(count_1) + int(count_2)
print(summa)

#number 4 - самая большая цифра в числе
chislo = int(input('Введите целое и положительное число'))
max_chislo = chislo % 10
while chislo >= 1:
    chislo = chislo // 10
    if chislo % 10 > max_chislo:
        max_chislo = chislo % 10
    if chislo > 9:
        continue
    else:
        print('Максимальное число', max_chislo)
    break

#number 5 - предприятие
print('Программа для оценки работы предприятия')
profit = float(input('Какова выручка предприятия за месяц? '))
waste = float(input('Каковы издержки предприятия за месяц? '))
if profit > waste:
    print(F'Предприятие работает с прибылью. Рентабильность равняется: {profit / waste:.2f}')
    personal = int(input('Сколько у вас сотрудников в предприятии ? '))
    print(F'Средняя зарплата одного сотрудника: {profit / personal:.2f}')
elif profit == waste:
    print("Предприятие работает в ноль")
else:
    print("Предприятие работает в убыток")

#number 6 - спортсмен
a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)