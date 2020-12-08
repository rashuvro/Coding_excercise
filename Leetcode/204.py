def prime_count(n):
    def prime(num):
        if num <=1:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    a = []
    for i in range(n+1):
        prime_num  = prime(i)
        if prime_num == True:
            a.append(prime_num)
    return len(a)
print(prime_count(499979))
