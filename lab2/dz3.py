def is_prime(number):
    s = 0
    for i in range(1, number+1):
        if number % i == 0:
            s += 1
        if s > 2:
            return False
    return True

n = int(input())

print(is_prime(n))