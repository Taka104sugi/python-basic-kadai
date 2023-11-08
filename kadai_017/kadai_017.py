class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f'{self.name}さんはお酒が飲めます。')
        else:
            print(f'{self.name}さんは未成年にはアルコールを販売できません。')

# Humanクラスのインスタンスをリストに追加
humans = []

while True:
    name = input("お名前を入力してください（終了するにはEnterキーを押してください）：")
    if not name:
        break

    age = int(input("ご年齢を入力してください："))
    human = Human(name, age)
    humans.append(human)

# リストの要素数分だけcheck_adultメソッドを呼び出す
for human in humans:
    human.check_adult()