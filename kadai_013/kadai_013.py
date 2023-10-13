price = int(input("商品の金額を入力してください:"))

tax = 1.1

def total_price(price, tax):
    total = price * tax
    print(f"{total}円になります")

total_price(price, tax)
