#这是作者在学习python条件判断和列表的时候写的作品
#一个可以打发五秒钟时间的小程序^~^
sx='猴鸡狗猪鼠牛虎兔龙蛇马羊'
year=int(input('请输入出生年份：'))
if (sx[year%12])=='猪':
  print('猪年风调雨顺')
elif(sx[year%12])=='猴':
    print('猴年风调雨顺')
elif (sx[year % 12]) == '鸡':
    print('鸡年吉祥如意')
elif(sx[year%12])=='狗':
    print('狗年财源滚滚')
elif(sx[year%12])=='鼠':
    print('鼠年子庶丰登')
elif(sx[year%12])=='牛':
    print('牛年牛气冲天')
elif(sx[year%12])=='虎':
    print('虎年虎啸年丰')
elif(sx[year%12])=='兔':
    print('兔年万事如意')
elif(sx[year%12])=='龙':
    print('龙年年老龙钟')
elif(sx[year%12])=='蛇':
    print('蛇年安康')
elif(sx[year%12])=='马':
    print('马年马到成功')
else:
    print('羊年喜气洋洋')