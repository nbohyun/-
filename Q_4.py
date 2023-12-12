def solution(r1, r2):
    answer = 0

    for i in range(1, r2+1): # for구문을 이용해 1부터 r2까지의 정수를 변수 i에 대입해 반복문을 실행함, i는 현재 반지름
        if i < r1: 
            y = int((r1**2 - i**2)**0.5) + 1 # x좌표에 대응하는 y좌표로 int를 이용하여 소수점 이하를 버린 후 1을 더함
        else:
            y = 0

        x = int((r2**2 - i**2)**0.5) # y좌표에 대응하는 x좌표로 int를 이용하여 소수점 이하를 버린 후 x에 대응함

        answer = answer + x - y + 1 # 해당 반지름에서의 정수 좌표를 answer에 누적

    return answer * 4 # 1사분면을 기준으로 정수인 점의 개수를 구했으므로 4를 곱함

print(solution(2, 3))  # 출력 결과: 20

