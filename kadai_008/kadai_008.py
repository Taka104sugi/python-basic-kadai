var = int(input("正の整数を入力してください: "))

elif var % 3 == 0:
    print("Fizz")
elif var % 5 == 0:
    print("Buzz")
if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")
else:
    print(var)