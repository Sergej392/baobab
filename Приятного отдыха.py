print("Введите текущую температура в градусах")
a = int(input())
c = (25 - a)
b = (20 - a)
if a > 25:
    print("Слишком жарко!Оптимальная температура на ",c," холоднее.Включаю кондиционер.Сейчас станет прохладнее.")
if a < 20:
    print("Слишком холодно!Оптимальная температура на ",b," теплее.Включаю обогреватель.Сейчас станет теплее.")
print("Приятного отдыха!")