import easygui as g
import sys
g.msgbox('第一次用python做桌面应用')
msg="你现在想干什么"
title="请选择"
choice=['睡觉','学习','撸代码']
#选择框的init
choice=g.choicebox(msg,title,choice)
g.msgbox('你的选择是:'+str(choice),"结果")
msg="你确定吗？"
if g.ccbox(msg,title):#show a continue/cancel
    pass
else:
    sys.exit(0)
