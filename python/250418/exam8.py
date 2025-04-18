def add(x, y = 10) : # y가 없을 때 디폴트 값
    print(x + y)
    
add(y = 3, x = 1) # 변수 명시 해주면 가능
add(1, 2)

add(30)

# list = [1,2,3,4,5]
# print(sum(list))

def add(*num) :
    print(num)
    return sum(num)

print(add(1, 2))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

def info(**user) :
    for key, value in user.items() :
        print(f"{key} : {value}")
    
    
info(name = '홍길동', age=30, addr='인천')

def test() :
    print(10)
    
test()