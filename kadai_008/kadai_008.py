var = int(input("正の整数を入力してください: "))

if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")
if var % 3 == 0 and var % 5 != 0:
    print("Fizz")
if var % 3 != 0 and var % 5 == 0:
    print("Buzz")