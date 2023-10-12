var = int(input("正の整数を入力してください: "))

if var % 3 == 0:
    print("Fizz")
elif var % 5 == 0:
    print("Buzz")
elif var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")

else:
    print(var)