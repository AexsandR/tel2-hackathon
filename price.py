prices_tariff = {
    1: 700,
    2: 500,
    3: 450,
    4: 400,
    5: 300,
    6: 890}
prices_tariff1 = {
    700: 1,
    500: 2,
    450: 3,
    400: 4,
    300: 5,
    890: 6}

#
def price(id):
    balance = prices_tariff[id]
    list_price = [300, 400, 450, 500, 700, 890]
    if id == 6:
        return False
    return prices_tariff1[list_price[list_price.index(balance) + 1]]


i = [0, 95]
minutes = min_price = abs(i[1])
min_price = (lambda x: x - 1 if x % 10 == 5 else x)(min_price)
min_price = (lambda x: x + 1 if x % 10 == 9 else x)(min_price)
min_price = ((lambda x: 1 if min_price // 50 > 0 else 0)(i) * min_price - 40) + 40
min_price -= min_price // 10 * 2
print(minutes, min_price)

# 55 - 44
# 60 - 48
# 70 - 56
# 80 - 64
# 85 - 68
# 90 - 72
# 100 - 80
