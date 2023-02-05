def evenum(number):
    return number%2==0

a = [0,1,2,3,4,5,6,7,8,9,10]
print(list(map(evenum,a)))
print(list(filter(evenum,a)))