money = 100000
per_cent = {"ТКБ": 5.6, "СКБ": 5.9, "ВТБ": 4.28, "СБЕР": 4.0}

a = list(per_cent.values())
deposit = []

for i in a:
    deposit.append(int((money * i)/100))

print(deposit)
print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)}')