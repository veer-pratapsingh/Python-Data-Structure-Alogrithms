def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()

def func(a):
    message=a("Hello How are you Guy's?")
    print(message)
    
func(lowercase)
func(uppercase)    
    