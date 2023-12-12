def solution(numbers):
	
    numbers_list = [str(x) for x in numbers] # 배열 number 안에 정의된 숫자를 문자열로 변환하여 리스트에 저장함  
    numbers_list.sort(key=lambda x: x*3, reverse=True) # sort함수를 이용하여 numbers_list 의 요소에 3을 곱한 후 순서대로 정렬함 
    answer = str(int(''.join(numbers_list))) # join 함수를 이용하여 리스의 값을 합쳐 문자열을 만들고 그 문자열을 정수로 반환한 뒤 다시 문자열로 반환함 
    return answer

numbers = [8, 30, 17, 2, 23]
result = solution(numbers)
print(result) # 출력 결과 : 803023217 
