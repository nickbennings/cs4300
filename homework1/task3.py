def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def sum_numbers_upto_100():
    total = 0
    num = 1
    while num <= 100:
        total += num
        num += 1
    return total

