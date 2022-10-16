money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
lack = 0

# TODO Оформить решение
while True:
    lack += salary - spend
    spend = spend * (1 + increase)
    money_capital += lack
    if (money_capital <= 0): break
    month += 1

print(month)