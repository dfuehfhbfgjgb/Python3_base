def fun01():
    print("执行方法fun01")

import time

# 返回当前时间戳（相对于1970年）

# print("%.2f"%time.time())
#
# # 返回当前时间
#
# # print(time.ctime())
# print(time.mktime(time.localtime()))
# print(time.localtime())
#
# print(time.strftime("%Y %m %d  %H:%M:%S %j", time.localtime()))
#
# print(time.strftime("%y %m %d  %H:%M:%S", time.localtime()))
#
# print(time.strptime("2019 05 12 14:55:00", "%Y %m %d %H:%M:%S"))
class Week:
    def print_time(self):
        year=int(input("请输入年份："))
        month=int(input("请输入月份："))
        day=int(input("请输入天数:"))
        return "%d %02d %02d"%(year,month,day)
    def str_week(self,data):
        week_dict={
            0:'星期一',
            1:'星期二',
            2:'星期三',
            3:'星期四',
            4:'星期五',
            5:'星期六',
            6:'星期日'
        }
        print(week_dict[data])
    def get_week(self):
        result=self.print_time()
        time_tuple=time.strptime(result,'%Y %m %d')
        self.str_week(time_tuple[6])

# w01=Week()
# w01.get_week()
