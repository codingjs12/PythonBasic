fruits = {'apple' : 1, 'banana': 2, 'cherry': 3}

menu = {'coffee': 1, 'tea': 2, 'juice': 3}

print(menu)
print(fruits)

print(fruits.keys())

print(fruits.values())
print(fruits.items())

num = int(input('숫자 입력: '))
# 입력값이 5보다 크면 '5보다 큽니다' 출력
if num > 5 :
    print('5보다 큽니다')
# 입력값이 5보다 작으면 '5보다 작습니다' 출력
elif num < 5 :
    print('5보다 작습니다')


# 숫자 하나를 입력 받아서 홀수, 짝수 구분

num = int(input('숫자 입력: '))
if(num % 2 == 0) :
    print('짝수입니다')
else :
    print('홀수입니다')
    
price = 20000    
age = int(input('나이 입력: '))

if age >= 60 :
    price = price * 0.5
    print('50% 할인된 금액 :', price)
elif age >= 6 : 
    print('정상 금액 :', price)
else :
    print('무료입니다')
    
    
if "apple" in fruits :
    print('apple 있음')
else :
    print('apple 없음')
    
    
txt = 'hello python'

if "python" in txt :
    print('python 있음')
    

hong = {'name': '홍길동', 'age': 20, 'address': '서울'}

if 'name' in hong :
    print('name 있음')

print(hong.values())

if '홍길동' in hong.values() :
    print('홍길동 있음')

if '인천' not in hong.values() :
    print('인천 없다.')
        
for i in range(10) :
    print(i, end=' ')

sum = 0

for i in range(1, 11) :
    sum += i # sum = sum + i

print('1부터 10까지의 합:', sum)



