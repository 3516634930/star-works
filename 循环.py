#sx='猴鸡狗猪鼠牛虎兔龙蛇马羊'
#for cz in sx:
#    print(cz)
#for year in range(2000,2022):
#    print('%s 年的生肖是 %s' %(year,sx[year%12]))
#上面的是if的循环
num=5
while True:
    print('a')
    num = num + 1
    if num>10:
       
#这里会输出六个a是因为如果num=5，则5+1到>10有六组数，当最后一组数>10的时候结尾的break就会起到作用把while给结束掉