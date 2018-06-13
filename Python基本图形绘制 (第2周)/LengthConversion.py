#米和英寸之间的长度转换
Length = input()
if Length[-1] in 'm':
    LengthChange = eval(Length[0:-1]) * 39.37
    print("{:.3f}in".format(LengthChange))
elif Length[-1] in 'n':
    LengthChange = eval(Length[0:-2]) / 39.37
    print("{:.3f}m".format(LengthChange))
else:
    print("输入的格式错误")