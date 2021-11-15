# 랜덤 무듈 불러오기
import random
import myModule as my

x = random.randint(0,1) # 0,1의 랜덤 숫자 생성
# 동전을 던졌을때 랜덤으로 앞 뒷면이 나오도록 코드 작성

if x == 1:
    print("앞면")
else:
    print("뒷면")

# 내가 만든 마이모듈의 변수 pi를 불러옴
print(my.pi)



# 랜덤모듈을 이용해 학생들중 한명을 당첨하여 점심값을 내게 하자.

# ​1. 학생들의 이름을 입력받는다.

# 2. 입력받은 문자열에서 이름들을 분리해 *리스트에 담기

# 3. 랜덤 함수를 이용해 학생들의 숫자에 맞는 랜덤정수를 만들어
#    당첨자를 선택한다. 리스트의 인덱스 번호 이용

# 🚨 여기는 그대로 👇
names_string = input("내기를 할 친구들의 이름을 적습니다. 콤마(,)로 분리해서 적습니다.\n")
names = names_string.split(",")
# 🚨 여기는 그대로 👆

#아래에 코드 작성 👇
# print(names)
#print(len(names))

n = random.randint(0, len(names)) # 랜덤 인덱스 숫자(사람수 만큼)

print(f"오늘 커피는{names[n]}가 쏩니다!")