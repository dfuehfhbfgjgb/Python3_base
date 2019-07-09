# 设计各种鸭子的类，包括绿头鸭、红头鸭、橡皮鸭、模型鸭，
# 所有的鸭子都能游泳和显示不同的外观，
# 红头鸭和绿头鸭会呱呱叫且会飞，
# 橡皮鸭会吱吱叫但不会飞，
# 模型鸭不会飞也不会叫。
class Duck:
    def skill(self,obj):
        print("%s能游泳"%obj.name)
    def show(self,obj):
        return obj.show()
    def action(self,obj):
        return obj.action()
class RedDuck(Duck):
    def __init__(self,name):
        self.name=name
    def show(self):
        print("头是红色")
    def action(self):
        print("会呱呱叫会飞")
class GreenDuck(Duck):
    def __init__(self,name):
        self.name=name
    def show(self):
        print("头是绿色")
    def action(self):
        print("会呱呱叫会飞")
class RubberDuck(Duck):
    def __init__(self,name):
        self.name=name
    def show(self):
        print("橡皮做的")
    def action(self):
        print("会吱吱叫但不会飞")
class ModelDuck(Duck):
    def __init__(self,name):
        self.name=name
    def show(self):
        print("鸭子模型")
    def action(self):
        print("不会叫也不会飞")

if __name__=="__main__":
    d=Duck()
    r=RedDuck('红头鸭')
    g=GreenDuck('绿头鸭')
    ru=RubberDuck('橡皮鸭')
    m=ModelDuck('模型鸭')
    d.skill(m)
    d.show(m)
    d.action(m)

