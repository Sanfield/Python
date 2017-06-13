try:
    f=open('hahah.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('进入Errot:'+str(reason))
except TypeError as reason:
    print('进入第二个Error:'+str(reason))
except:
    
finally:
    print('国足进球了！！')
