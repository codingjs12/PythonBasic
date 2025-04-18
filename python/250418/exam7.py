#up and down

import random

number = random.randint(1, 100)

count = 0
while True:
    count = count + 1
    answer = int(input("1~100 숫자 : "))
    if answer < number :
        print("UP")
    elif answer > number :
        print("DOWN")
    elif answer == number :
        print("정답입니다.")
        print(f"{count}번 만에 맞췄습니다.")
        break
    else:
        print("잘못된 입력입니다.")
        continue
    
    
