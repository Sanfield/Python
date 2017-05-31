print("踩一个数字")
temp = input("猜呀")
guss = int(temp)
while guss!=8:
    temp = input("不对。请再试一次")
    guss= int(temp)
    if guss == 8:
        print("duile")
    else:
        if guss >8:
            print("big")
        
        else:
            print("small")
print("game over")
