# 실습2) 유저 DB 갱신 프로그램

# dictionary 변수 선언
dicUser = {} 

# 사용자 정보 input 함수
def userInfo(comment):
  val = input(comment)
  return val

# userInfo 함수를 이용하여 input 받음
name = userInfo('이름: ')
age = userInfo('나이: ')
phone = userInfo('연락처: ')

# dicUser 딕셔너리에 input 받은 값 업데이트
dicUser.update({'name': name})
dicUser.update({'age': age})
dicUser.update({'phone': phone})

# 출력
print(dicUser)