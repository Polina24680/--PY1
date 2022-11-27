salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
delta_need = spend - salary
need = 0
# TODO Оформить решение
for i in tuple(range(1,10)):
    spend = spend * (increase+1)
    need = need + spend - salary

need_money = delta_need + need

print(round(need_money))
