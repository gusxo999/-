def basic():
    # 개인정보
    while 1:
        age = int(input("나이 : "))
        tall = float(input("키 : "))
        wei = float(input("몸무게 : "))
        mus = float(input("근육량 모르면 0 입력(평균치로 계산) : "))
        while 1:
            if mus == 0:
                sex = int(input("남자 = 1 여자 = 2 : "))
                if sex == 1:
                    mus = 28.0
                    str_sex = "남자"
                    break
                elif sex == 2:
                    mus = 20.0
                    str_sex = "남자"
                    break
                else :
                    print("오류")
                    continue
            else:
                sex = int(input("남자 = 1 여자 = 2 : "))
            if sex == 1:
                str_sex = "남자"
                break
            elif sex == 2:
                str_sex = "남자"
                break
            else:
                print("오류")
                continue
        break
    

    # BMC 기초대사량 == 섭취 칼로리
    if sex == 1:
        BMC = 66.47 + (13.75 * wei) + (5 * tall) - (6.76 * age)
    else :
        BMC = 665.1 + (9.56 * wei) + (1.85 * tall) - (4.68 * age)
     
    
    # Act_BMC 활동대사량
    Act_BMC = 0
    Act_lev = int(input("주당 운동하는 시간 :"))
    if 0 < Act_lev < 2:
        Act_BMC = BMC + int((BMC * 0.3))
        print("당신의 활동량은 낮은 수준입니다.")
    elif 2 <= Act_lev < 5:
        Act_BMC = BMC + int((BMC * 0.5))
        print("당신의 활동량은 중간 수준입니다.")
    elif Act_lev >= 5:
        Act_BMC = BMC + int((BMC * 0.75))
        print("당신의 활동량은 높은 수준입니다.")
        
    # 식단 목적
    what = int(input("식단 목적 다이어트 = 0, 증량 = 1, 유지 = 2"))
    if what == 0:
        print("식단의 목적 : 다이어트")
    elif what == 1:
        print("식단의 목적 : 증량")
    elif what == 2:
        print("식단의 목적 : 유지")

    # Diet == 활동 대사량 - 500 
    my_protein = wei * 2 # 섭취 단백질 g
    protein = int(my_protein) * 4 # 단백질 kcal 
    Diet_kcal = Act_BMC - 500
    BMC_1 = Diet_kcal - protein # 단백질 칼로리를 제외한 활동 칼로리    
    carb = int((BMC_1 * 0.7)) # 탄수화물 kcal 

    fat = int(BMC_1 * 0.3) # 지방 kcal 
    my_carb = int(carb / 4) #탄수화물 g

    my_fat = int(fat / 9) # 지방 g 

    
    # 증량 == 활동 대사량 + 100 
    # Up_kcal = Act_BMC + 100
    
    # 유지 == 활동 그대로
    # Keep_kcal = Act_BMC


#     # 출력
#     print(f"성별 : {str_sex}, 나이 : {age}, 키 : {tall}, 몸무게 : {wei}, 근육량 : {mus}")
    print(f"기초 대사량 : {BMC}kcal,\
    필요 단백질 : {my_protein}g, 필요 탄수화물 : {my_carb}g, 필요 지방 : {my_fat}g")
#     print("섭취 칼로리")
    print(f'기초 대사량 : {BMC}kcal, 섭취 열량 : {Diet_kcal:.1f}kcal, \n, \
    탄수화물 : {carb}kcal, 단백질 : {protein}kcal, 지방 : {fat}kcal')
#     print()
#     print("프로토타입이기에 섭취 단백질은 체중 * 2g 탄수화물 및 지방 비율은 7:3으로 고정 향후 수정")
#     print()
    
    # 밥 탄35 단3 지- 칼300
    # 닭찌 4 22 1.9 120
    # 아몬드 20, 21.26, 50.64, 578
    
    
    rice_tan = 35
    chicken_dan = 22
    amond_zi = 5
    
    eat_chi = my_protein / chicken_dan
    eat_rice = my_carb / rice_tan
    eat_amon = my_fat / amond_zi
    
    
    
    print(f'먹어야 할 밥 양({eat_rice * 100:.1f}g), 먹어야 할 닭찌 양({eat_chi * 100:.1f}g), 먹어야 할 아몬드 갯수{eat_amon :.1f}')
    

basic()