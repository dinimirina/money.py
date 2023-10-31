money = int(input('Введите сумму вклада'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(per_cent[key] * money / 100)
max_deposit = max(deposit)
print(deposit)
print ("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))


years = int(input('Введите количество лет: '))
total_money = max_deposit * (1 + max(deposit) / 100) ** years
print("Итоговая сумма после " + str(years) + " лет составит " + str(total_money))
