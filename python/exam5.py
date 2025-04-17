list = [0] * 100 # 리스트에 0을 100개 넣음

print(list)

list = [i for i in range(1, 100+1)] # 리스트에 1부터 100까지 넣음

print(list)

list = [int(input(f"{i}번째 정수 입력 : ")) for i in range(1, 5+1)]

print(list)

list = []
for i in range(1, 5+1) :
    list.append(int(input(f"{i}번째 정수 입력 : ")))
print(list)

list = [0] * 5
for i in range(len(list)) :
    list[i] = int(input(f"{i+1}번째 정수 입력 : "))
print(list)