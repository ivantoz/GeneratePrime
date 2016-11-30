def gen_primes(n):
    lower = 0;
    for num in range(lower, n + 1):
        # prime numbers are greater than 1
        if n > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
        else :
            return 'No negative prime numbers'


gen_primes(15)