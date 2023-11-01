class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name, self.age)

# Humanクラスのインスタンスを作成
human = Human("太郎", 25)

# メソッドを呼び出して属性を出力
human.printinfo()

