# 실습1) 시험 점수 자동 채점 프로그램

# 기준 변수 설정
cut = 65
maximum = 100
minimum = 0

# 점수 입력
num1 = int(input('창사코: '))
num2 = int(input('선형대수: '))
num3 = int(input('컴퓨터공학: '))

# 입력 확인 (출력)
print('점수', num1, num2, num3)

# 셋 중 하나라도 100보다 큰 수가 입력된 경우 -> 잘못 입력
if num1 > maximum or num2 > maximum or num3 > maximum:
  print('잘못된 점수가 입력되었습니다. (100 이상)')

# 셋 중 하나라도 0보다 작은 수가 입력된 경우 -> 잘못 입력
elif num1 < minimum or num2 < minimum or num3 < minimum:
  print('잘못된 점수가 입력되었습니다. (0 이하)')

# 모두 65점을 넘은 경우 -> 합격
elif num1 > cut and num2 > cut and num3 > cut:
  print('합격입니다.')

# 그렇지 않을 경우 -> 불합격
else:
  print('불합격입니다. 재수강 하세요.')