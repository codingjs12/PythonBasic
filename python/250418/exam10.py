x = 10

def test() :
   global x
   x = 20
test()

print(x)

def fact(x) :
    value = 1
    for i in range(x, 0, -1) :
        value *= i
    print(value)
    
fact(5)

def fact(x) :
    if x == 0 :
        return 1
    else :
        return x * fact(x - 1)

print(fact(4))


