#美元与人民币转换
Currency = input()
if Currency[0:3] in 'USD':
    Money = eval(Currency[3:]) * 6.78
    print("RMB{:.2f}".format(Money))
if Currency[0:3] in 'RMB':
    Money = eval(Currency[3:]) / 6.78
    print("USD{:.2f}".format(Money))
else:
    print("输入格式错误")