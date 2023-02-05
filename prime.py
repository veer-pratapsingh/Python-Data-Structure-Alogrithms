def check (numbers):
    primeNumber = []
    for number in numbers:
        if number>1:
            for i in range (2, int(number/2)+1):
                if (number % i) == 0:#If number is divisible by any number between 2 and number / 2, it is not prime
                    print (number, "is not a prime number")
                break
            else:
                print (number, "iş a prime number")
                primeNumber.append(number)
        else:
            pass
    return primeNumber

check([2,3,4,5,6,7,8,9,10,11,12,13,14,15])
