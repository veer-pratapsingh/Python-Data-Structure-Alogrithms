a = int(input("Enter the value of A:"))
b = int(input("Enter the value of B:"))
add = a+b
sub = a-b
mul = a*b
div = a/b
print("SUM = %d, SUB = %d, MUL = %d, DIV = %15.3f"%(add,sub,mul,div))#Using THE PADDING AND PRECISION
print('{0:<4} | {1:<4} | {2:<4} | {3:<4}'.format('SUM','SUB','MUL','DIV'))
print('{0:<4} | {1:<4} | {2:>4} | {3:>4}'.format(add,sub,mul,div))#For creating table like representation