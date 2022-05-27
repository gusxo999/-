#!/usr/bin/env python
# coding: utf-8

# In[23]:


# 입력 함수 
# 이름, 나이, 성별, 키, 몸무게, 근육량
def Main_Data():
    arr_data = []
    arr_data.append(input("아이디 : ")) # 0
    arr_data.append(int(input("나이 : "))) # 1
    arr_data.append(int(input("성별 : 남자(1), 여자(2)"))) # 2
    arr_data.append(float(input("키 : "))) # 3
    arr_data.append(float(input("체중 : "))) # 4
    arr_data.append(float(input("근육량 : 모르면 0 입력"))) # 5
    arr_data.append(int(input("주당 운동 시간 : "))) # 6
    if arr_data[5] == 0:
        if arr_data[2] == 1:
            arr_data[5] = 28.0
            arr_data[2] = "남자"
        else:
            arr_data[5] = 20.0
            arr_data[2] = "여자"    
    else:
        if arr_data[2] == 1:
            arr_data[2] = "남자"
        else:
            arr_data[2] = "여자"
    print()
    print(f"이름 : {arr_data[0]}")
    print(f"나이 : {arr_data[1]}")
    print(f"성별 : {arr_data[2]}")
    print(f"키 : {arr_data[3]}")
    print(f"체중 : {arr_data[4]}")
    print(f"근육량 : {arr_data[5]}")
    print(f"주당 활동 시간 : {arr_data[6]}")
    print()
    return(arr_data)

# 기초 대사량 (BMC), 활동 대사량(Act_BMC)
def BMC(): 
    if user_data[2] == "남자":
        BMC = 66.47 + (13.75 * user_data[5]) + (5 * user_data[3]) - (6.76 * user_data[1])
    else : # 여자
        BMC = 665.1 + (9.56 * user_data[5]) + (1.85 * user_data[3]) - (4.68 * user_data[1])
    # 활동 대사량(Act_BMC)
    Act_lev = user_data[6]
    if 0 < Act_lev < 2:
        Act_BMC = BMC + int((BMC * 0.3))
        Low = Act_BMC
        lev = "low"
        print("당신의 활동량은 낮은 수준입니다.")
        return(Low, lev)
    elif 2 <= Act_lev < 5:
        Act_BMC = BMC + int((BMC * 0.5))
        Normal = Act_BMC
        lev = "normal"
        print("당신의 활동량은 중간 수준입니다.")
        return(Normal, lev)
    elif Act_lev >= 5:
        Act_BMC = BMC + int((BMC * 0.75))
        High = Act_BMC
        lev = "high"
        print("당신의 활동량은 높은 수준입니다.")
        return(High, lev)
    


# 식단 목적별 분류
def What(Act_BMC, lev):
    what = int(input("식단 목적 다이어트 = 0, 증량 = 1, 유지 = 2"))
    meal = []
    protein = user_data[4] * 2 # 섭취 단백질량
    if what == 0:
        print("식단의 목적 : 다이어트")
         # Diet == 활동 대사량 - 500 
        Diet_kcal = Act_BMC - 500
        BMC_Diet = Diet_kcal - (protein * 4) # 단백질 칼로리를 제외한 활동 칼로리    
        carb = int((BMC_Diet * 0.7)) # 탄수화물 kcal         
        fat = int(BMC_Diet * 0.3) # 지방 kcal         
        my_carb = int(carb / 4) #탄수화물 g       
        my_fat = int(fat / 9) # 지방 g 
        meal.append(Diet_kcal)
        meal.append(BMC_Diet)
        meal.append(carb)
        meal.append(fat)
        meal.append(my_carb)
        meal.append(my_fat)
        print(f"총 칼로리 :{meal[0]}")
        print(f"섭취 탄수화물 :{meal[4]}g")
        print(f"섭취 단백질 :{protein}g")
        print(f"섭취 지방 :{meal[5]}g")        
        return(meal)
        
        # 증량 == 기본 양식 활동 대사량 + 100 활동량에 따라 변화
    elif what == 1:
        print("식단의 목적 : 증량")
        # Act_lev == 낮음       
        if lev == "low":
            print("활동량이 낮기 때문에 활동 대사량 + 300kcal에서 시작합니다")
            Plus_300_kcal = Act_BMC + 300
            BMC_Plus = Plus_300_kcal - (protein * 4) # 단백질 칼로리를 제외한 활동 칼로리    
            carb = int((BMC_Plus * 0.7)) # 탄수화물 kcal 
            fat = int(BMC_Plus * 0.3) # 지방 kcal 
            my_carb = int(carb / 4) #탄수화물 g
            my_fat = int(fat / 9) # 지방 g
            meal.append(Plus_300_kcal)
            meal.append(BMC_Plus)
            meal.append(carb)
            meal.append(fat)
            meal.append(my_carb)
            meal.append(my_fat)
            print(f"총 칼로리 :{meal[0]}")
            print(f"섭취 탄수화물 :{meal[4]}g")
            print(f"섭취 단백질 :{protein}g")
            print(f"섭취 지방 :{meal[5]}g") 
            return(meal)
                
        # Act_lev == 중간    
        elif lev == "normal":
            print("활동량이 적당하기 때문에 활동 대사량 + 400kcal에서 시작합니다")
            Plus_400_kcal = Act_BMC + 300
            BMC_Plus = Plus_400_kcal - (protein * 4) # 단백질 칼로리를 제외한 활동 칼로리    
            carb = int((BMC_Plus * 0.7)) # 탄수화물 kcal 
            fat = int(BMC_Plus * 0.3) # 지방 kcal 
            my_carb = int(carb / 4) #탄수화물 g
            my_fat = int(fat / 9) # 지방 g
            meal.append(Plus_400_kcal)
            meal.append(BMC_Plus)
            meal.append(carb)
            meal.append(fat)
            meal.append(my_carb)
            meal.append(my_fat)
            print(f"총 칼로리 :{meal[0]}")
            print(f"섭취 탄수화물 :{meal[4]}g")
            print(f"섭취 단백질 :{protein}g")
            print(f"섭취 지방 :{meal[5]}g") 
            return(meal)
                
        # Act_lev == 높음
        elif lev == "high":
            print("활동량이 높기 때문에 활동 대사량 + 500kcal에서 시작합니다")
            Plus_500_kcal = Act_BMC + 300
            BMC_Plus = Plus_500_kcal - (protein * 4) # 단백질 칼로리를 제외한 활동 칼로리    
            carb = int((BMC_Plus * 0.7)) # 탄수화물 kcal 
            fat = int(BMC_Plus * 0.3) # 지방 kcal 
            my_carb = int(carb / 4) #탄수화물 g
            my_fat = int(fat / 9) # 지방 g
            meal.append(Plus_500_kcal)
            meal.append(BMC_Plus)
            meal.append(carb)
            meal.append(fat)
            meal.append(my_carb)
            meal.append(my_fat)
            print(f"총 칼로리 :{meal[0]}")
            print(f"섭취 탄수화물 :{meal[4]}g")
            print(f"섭취 단백질 :{protein}g")
            print(f"섭취 지방 :{meal[5]}g") 
            return(meal)

user_data = []
user_data = Main_Data()
Act_BMC, lev = BMC()
meal_data = []
meal_data = What(Act_BMC, lev)


# In[19]:


a = 1
b = 2
c = 3
arr = []
arr.append(a)
arr.append(b)
arr.append(c)
print(arr)


# In[ ]:




