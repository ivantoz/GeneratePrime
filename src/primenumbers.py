def generate_prime(n):
    if isinstance(n, int):
        if n < 0 :
            return 'Negative numbers cannot be prime numbers'
        elif n < 2 :
            return 'No prime number below 2'
        else:
            prime = []
            for num in range(2, n + 1):
                for i in range(2, num):
                    if (num % i == 0):
                        break
                else:
                    prime.append(num)
            return prime

    else:
        return 'Cannot find prime of non integer'



