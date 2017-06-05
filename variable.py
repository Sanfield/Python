def discounts(price,rate):
    final_price = price *rate
    return final_price
old_price = float(input("请输入原价:"))
rate =float(input("请输入折扣率:"))
new_price=discounts(old_price,rate)
print("打折后的价格是:",new_price)
