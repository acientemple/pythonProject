# -*- coding: utf-8 -*-

print('请输入您的体重和身高')
w=input('您的体重是（千克）：')
h=input('您的身高是：厘米')
weight=float(w)
height=float(h)
s1=height*height/10000*18.5
s2=height*height/10000*25
bmi=weight/(height*height/10000)

if bmi<18.5:
    print('过轻! 您至少需要增重%.2f公斤。'%(s1-weight))
elif bmi<25:
    print('恭喜你，体重正常，继续保持！')
elif bmi<32:
	print('肥胖! 您至少需要减肥%.2f公斤。'%(weight-s2))
else:
	print('过分了! 您需要减肥%.2f--%.2f公斤。'%(weight-s2,weight-s1))