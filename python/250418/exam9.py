def score(kor, eng, math) :
    sum = kor + eng + math
    avg = sum / 3
    
    return sum, avg

print(score(100, 92, 93))

total, average = score(90, 95, 99)

print(total)

print(f"{average:.2f}")