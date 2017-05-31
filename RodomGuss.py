import random
secret = random.randint(1,10)
print("踩一个数字")
temp = input("猜呀")
guss = int(temp)
while guss!=secret:
    temp = input("不对。请再试一次")
    guss= int(temp)
    if guss == secret:
        print("duile")
    else:
        if guss > secret:
            print("big")
        
        else:
            print("small")
print("game over")
