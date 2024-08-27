# попробуем по другому
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [0]
not_primes = [0]
for i in numbers:
    a = True
    for k in range(2, i):
        if i % k == 0:
            a = False
            break
    if a:
        primes . append(i)
    else:
        not_primes . append(i)
print(primes)
print(not_primes)














    





























         


    























