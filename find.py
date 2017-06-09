f=open("F:\\python\\file\\file2.txt")
sang=[]
fei=[]
for eachline in f:
    (role,line_speak)=eachline.split(':',1)
    if role=='桑':
        sang.append(line_speak)
    if role=='飞':
        fei.append(line_speak)
sang_file= open("F:\\python\\file\\sang_file.txt",'w')
fei_file=open("F:\\python\\file\\fei_file.txt",'w')
sang_file.writelines(sang)
fei_file.writelines(fei)
sang_file.close()
fei_file.close()
sang=[]
fei=[]

f.close()
