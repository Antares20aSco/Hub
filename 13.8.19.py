Ticket_sum = int(input('Введите количество билетов:')) # ввод количества билетов
prices = []
price = 0
for i in range(Ticket_sum): # определение цен для билетов
    age = int(input('Введите возраст:')) # ввод возраста
    if age < 18:
        price = 0
        print('Бесплатно')
    elif 18 <= age < 25:
        price = 990
        print('Цена - ', price)
    elif 25 <= age:
        price = 1390
        print('Цена - ', price)
    prices.append(price)
sum_price = float(sum(prices))
print('Сумма - ', sum_price)
if Ticket_sum > 3:
    total = sum_price * 0.9
    print('Ваша скидка - 10%. Сумма к оплате - ', total)
else:
    print('Сумма к оплате - ', sum_price)
