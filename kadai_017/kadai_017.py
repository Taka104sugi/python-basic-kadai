while True:
    name = input("お名前を入力してください：")
    age = int(input("ご年齢を入力してください："))

    if age <= 20:
        print("20歳以下なので終了します。")
        break

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        if self.age >= 20:
            print('お酒が飲めます。')
        else:
            print('未成年にはアルコールを販売できません。')

# Humanクラスのインスタンスを作成
human = Human(name, age)

# メソッドを呼び出して属性を出力
human.printinfo()