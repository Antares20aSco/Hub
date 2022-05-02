money = float(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = per_cent.get('ТКБ')
SKB = per_cent.get('СКБ')
VTB = per_cent.get('ВТБ')
SBER = per_cent.get('СБЕР')
TKB_d = round(money*TKB/100, 2)
SKB_d = round(money*SKB/100, 2)
VTB_d = round(money*VTB/100, 2)
SBER_d = round(money*SBER/100, 2)
deposit = [TKB_d, SKB_d, VTB_d, SBER_d]
print(deposit)
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))
