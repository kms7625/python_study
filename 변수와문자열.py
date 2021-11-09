'''
# 여러개의 변수를 동시에 초기화
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
# 예제 2 ~ 5 풀기
# 2
x = 10
print(x)
# 3
x, y, z = 1, 2, 3
print(x, y, z)  # 출력시 변수 여러개 가능
# 4
x, y, z = 1, 1.1, "1"
print(type(x), type(y), type(z))
#  5 🚨 여기 코드는 수정 안합니다.👇
a = input("a: ")
b = input("b: ")
# 🚨 여기 코드는 수정 안합니다. 👆
####################################
# 여기에 a,b 값을 바꾸는 코드 작성 👇
a, b = b, a
# 여기에 a,b 값을 바꾸는 코드 작성 👆
####################################
# 🚨 여기 코드는 수정 안합니다. 👇
print("a: " + a)
print("b: " + b)
# 🚨 여기 코드는 수정 안합니다. 👆
'''


# 문자열

# 긴 문자열은 따옴표 3개(''', """)
var3 = '''
'따옴표' 3개는
끝나는 "문장"까지
모두를 문자열로 처리
-----------------!
'''
# print(var3)

# 문자열 (+) 연산
성 = '홍'
이름 = '길동'
name = 성 + ' ' + 이름

# print(name)

# 타입 변환 : str(), int(), float()

# print(type(int(str(100))))

# 예제1
str1 = '\tIt\'s "kind of" sunny\n Have a nice Day!'
print(str1)

# 예제2
str2 = '''
다스베이더가 말했다.
    "내가 니 애비다!"
그 말을 들은 루크는 '깜짝' 놀랐다.
'''
print(str2)

# 예제3

#1. 밴드 이름 만들기 프로그램 환영합니다
print("밴드 이름 만들기 프로그램에 환영합니다.")

#2. 유저에가 태어난 도시를 물어봅니다.
city = input('태어난 도시가 어디인가요 ?\n')

#3. 유저에게 애완동물의 이름을 물어봅니다.
petName = input('애완 동물은 이름은 ?\n')

#4. 도시와 애완동물 이름을 조합하여 밴드이름을 만들어 출력합니다.
print('당신의 밴드 이름은 '+city + ' '+petName)

# 힌트: 문자열에 \n을 붙이면 한줄 뛰웁니다. => 문자열 입력을 받을때 한줄 아래로 커서이동