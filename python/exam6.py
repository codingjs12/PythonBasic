import random

list = [10, 5, 2, 30, 15]

print(max(list)) # 리스트에서 최대값을 찾음

print(random.randint(1, 10))

while True:
    x = random.randint(2, 9)
    y = random.randint(1, 9)
    
    print(f"{x} x {y} = ?")
    answer = int(input("정답 입력 : "))
    
    if answer == x * y:
        print("정답")
    elif answer == 0:
        print("종료")
        break
    else:
        print("오답")
    
while True:
    x = random.randint(2, 9)
    y = random.randint(1, 9)
    ans = int(input(f"{x} * {y} = "))
    
    if ans == 0:
        print("종료")
        break
    elif ans == x * y:
        print("정답")
    else:
        print("오답")

