
def fizzBuzz():
    for i in range(1, 101):
        res = ""
        if i % 3 == 0:
            res += "Fizz"
        if i % 5 == 0:
            res += "Buzz"
        if len(res) == 0:
            res += str(i)
        print(res)
