# fact=dict()
# fact["code"]='fun'
# print(fact["code"])
#
# bill = ({"cc":"22","l":"ee"})
# # if "cc" in bill:
#     # print('true')
# del bill["l"]
#
# print(bill)
#上面的是学习的时候记下来的一点笔记

fanxing=({"1":"红",
          "2":"红",
          "3":"蓝",
          "4":"红",
          "5":"蓝",
          "6":"蓝",})

n=input('输入1-6，抽选红蓝方：')
if n in fanxing:
    print(fanxing[n])
else:
    print('请输入1-6，请输入1-6，请输入1-6，重要的事情说三遍')