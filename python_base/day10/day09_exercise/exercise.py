# （3）、设计下面相关的功能类。
# 星巴克咖啡冲泡法：
# 1.净水煮沸；2.用沸水冲泡咖啡3.将咖啡倒入杯子4.加奶和糖
# 冲泡茶方法：
#     1. 净水煮沸；2.用沸水冲泡茶3.将茶倒入杯中4.加柠檬
class BrewDrinks:
    """
        冲泡饮料类
    """
    def first_step(self):
        print("净水煮沸")

    def second_step(self,obj):
        print("用沸水冲泡%s"%obj.name)

    def third_step(self,obj):
        print("将%s倒入杯子"%obj.name)

    def fourth_step(self,obj):

        return obj.fourth_step()

class BreakCoffee(BrewDrinks):
    """
        星巴克咖啡类
    """
    def __init__(self,name):
        self.name=name
    def fourth_step(self):
        print('加奶和糖')

class BreakTea(BrewDrinks):
    """
        冲泡茶类
    """
    def __init__(self,name):
        self.name=name
    def fourth_step(self):
        print('加柠檬')
if __name__=="__main__":
    c=BreakCoffee('星巴克咖啡')
    t=BreakTea('茶')
    b=BrewDrinks()
    b.first_step()
    b.second_step(t)
    b.third_step(t)
    b.fourth_step(t)