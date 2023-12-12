def solution(letter):
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    } # 각각의 모스부호와 소문자 알파벳을 쌍으로 묶은 morse라는 이름의 딕셔너리 생성함
    
    letter = letter.split() # 문자열을 나누는 split 함수를 이용하여 변수 letter를 공백을 기준으로 문자열을 분리함 
    letter_list = [morse[code] for code in letter] # 리스트 컴프리헨션을 이용하여 letter에 들어있는 모스부호와 대응하는 값을 morse 딕셔너리에 추출하여 letter_list를 생성함    
    answer = "".join(letter_list) # join 함수를 이용하여 문자열을 삽입함    
    return answer

print(solution("-. . ...- . .-. --. .. ...- . ..- .--. ")) # 출력 결과: nevergiveup

