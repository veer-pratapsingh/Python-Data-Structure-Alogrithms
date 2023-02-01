def function(n):
    if n>2:
        return n*function(n-1)
    else:
        return n
print(function(5))


      