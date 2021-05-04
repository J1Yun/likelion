# 실습3) 과일,채소 프로그램

# 기존 DB 설정
fruit = ['사과','오렌지','포도','파인애플']
vegetable = ['당근','호박','양상추','브로콜리']

# 카테고리와 상품명 입력
cate = input('등록할 카테고리를 선택해주세요 (과일/채소): ')
name = input('등록할 상품명을 입력하세요: ')

# 카테고리가 채소일 경우
if cate == '채소':

  # 상품명이 기존 DB에 존재할 경우 -> 등록 X
  if name in vegetable:
    print('이미 등록된 채소입니다.')
  # 상품명이 기존 DB에 존재하지 않을 경우 -> 등록
  else:
    vegetable.append(name)

# 카테고리가 과일일 경우
elif cate == '과일':

  # 상품명이 기존 DB에 존재할 경우 -> 등록 X
  if name in fruit:
    print('이미 등록된 과일입니다.')
  # 상품명이 기존 DB에 존재하지 않을 경우 -> 등록
  else:
    fruit.append(name)

# 카테고리가 과일 또는 채소가 아닐 경우 -> 잘못 입력
else:
  print('존재하지 않는 카테고리입니다.')

# 과일, 채소 리스트 출력
print(fruit, vegetable)
