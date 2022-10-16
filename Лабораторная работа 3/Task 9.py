salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
lack = 0

for i in range(10):
    lack += salary - spend
    spend = spend * (1 + increase)

need_money = abs(lack)
print(round(need_money))
