
try:
    print(x)
except:
    print("Variable x is not defined")
else:
    print ("Everything went wrong")
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")