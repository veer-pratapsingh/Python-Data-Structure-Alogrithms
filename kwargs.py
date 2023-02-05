def func(**kwargs):
    if 'name' in kwargs:
        print("The name is {0}".format(kwargs['name']))
    if 'age' in kwargs:
        print("The age is {0}".format(kwargs['age']))
    else:
        print("No key found")
        
func(name='vansh',age=24)            