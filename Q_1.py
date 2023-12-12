def solution(my_string, target):
	answer = 0 
	if (1 <= len(my_string) <= 100 and 1 <= len(target) <= 100): # if 조건문과 비교연산자를 이용하여 my_string 길이와 target의 길이를 1부터 100으로 제한함 
		if target in my_string: # if 조건문을 이용하여 target이 my_string 안에 있을때
			answer = 1 # 조건문이 참이면 1
		else:
			answer = 0 # 조건문이 거짓이면 0
	return answer 

print(solution("hello java world","java")) # solution 함수에 hello java world , java 라는 인수를 대입해 리턴값을 출력, 출력 결과 : 1
print(solution("I love you", "java")) # solution 함수에 I love you, java 라는 인수를 대입해 리턴값을 출력, 출력 결과 : 0  
