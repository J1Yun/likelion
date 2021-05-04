# 과제) 과일, 채소 프로그램 함수화

# 기존 DB 설정
fruit = ['사과','오렌지','포도','파인애플']
vegetable = ['당근','호박','양상추','브로콜리']

# 사용자로부터 입력받기 위한 함수
def WriteItem():
    category = input('등록할 카테고리를 선택해주세요 (과일/채소): ')
    if category != '채소' and category != '과일':
        return 0, 0
    item = input('등록할 상품명을 입력하세요: ')
    return category, item

# 제품 중복확인 함수
def ExistItem(category, item):
    if category == '채소':
        if item in vegetable:
            return 0
        else:
            return 1
    elif category == "과일":
        if item in fruit:
            return 0
        else:
            return 1
        
# 해당 카테고리 목록 반환 함수
def GetShowList(category):
    print("다음은 %s 카테고리 목록입니다." %category)
    if category == '채소':
        print(vegetable)
    elif category == "과일":
        print(fruit)

# 카테고리별 제품 등록 함수
def AddNew():
    cate, name = WriteItem()
    if cate == 0:
        print("존재하지 않는 카테고리입니다.")
        return 0
    exist = ExistItem(cate, name)
    if exist == 0:
        print("이미 등록되어있는 상품입니다.")
    elif cate == "채소":
        vegetable.append(name)
        GetShowList(cate)
    else:
        fruit.append(name)
        GetShowList(cate)

AddNew()
        
        
    