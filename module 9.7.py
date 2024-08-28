def is_prime(func):
    def wrapper(*numbers: int):
        res = func(*numbers)
        for i in range(1, res):
            if res % i == 0:
                print("Простое")
                return res
            else:
                print("Составное")
                break
    return wrapper



@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3

result = sum_three(2, 3, 6)
print(result)