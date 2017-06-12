import pickle
list1=[1321,456,48,'桑飞',['哈哈','hre']]
pick_file=open('F:\\python\\file\\list1.pkl','wb')
pickle.dump(list1,pick_file)
pickle.close()
pick_file.close()
