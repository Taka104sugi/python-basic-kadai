onamae = input("お名前を入力してください：")
nenrei = input("ご年齢を入力してください：")

class Human():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def humanname(self):
        print(self.name)
    def humanage(self):
        print(self.age)

printinfo = Human(onamae, nenrei)

printinfo.humanname
printinfo.humanage
