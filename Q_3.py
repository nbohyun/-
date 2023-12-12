def solution(age):
	if age > 1000:
		print("오류")
		return
	alphabet = {'0' : 'a', '1' : 'b', '2' : 'c', '3' : 'd', '4' : 'e', '5' : 'f', '6' : 'g', '7' : 'h', '8' : 'i', '9' : 'j'} # 딕셔너리를 이용하여 각각의 숫자와 알파벳을 대응시킴        
	age_list = [alphabet[i] for i in str(age)] # 리스트 컴프리헨션을 이용하여 age 변수에 들어있는 숫자를 문자열로 반환하고 그 문자열에 대응하는 값을 딕셔너리에 추출하여 age_list를 생성함
	answer = ''.join(age_list) # join 함수를 이용하여 문자열을 삽입함

	return answer 

print(solution(458)) # 출력 결과: efi
print(solution(21)) # 출력 결과 : cb
print(solution(1100)) # 출력 결과 : 오류

