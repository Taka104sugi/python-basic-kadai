var = int(input("正の整数を入力してください: "))

if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")
elif var % 3 == 0 and var % 5 != 0:
    print("Fizz")
elif var % 3 != 0 and var % 5 == 0:
    print("Buzz")
else:
    print(var)