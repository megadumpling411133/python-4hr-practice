# if conditional statement

# 1.
# 如果 肚子餓:
#   就去吃飯 < 內容縮排

#if 肚子餓:
#    就去吃飯

hungry = True
if hungry:
    print("就去吃飯")

# 2.
# 如果 下雨:
#   就開車上班
# 否則:
#    走路去上班

rainy = True
if rainy:
    print("開車上班")
else:
    print("走路上班")

# 3.
# 如果 考100分:
#   給你1000
# 或是如果 考80以上:
#   給你500
# 或是如果 考60以上:
#   給你100
# 否則:
#   給我300
score = 99
if score == 100:
    print("給你1000")
elif 100 > score >= 80:
    print("給你500")
elif 80 > score >= 60:
    print("給你100")
else:
    print("給我300")

# python 直譯式 從上往下 判斷完上面就往下走 已經判斷過的條件不需要再次判斷
score = 99
if score == 100: # False != 100 往下走
    print("給你1000") 
elif score >= 80: # True (!= 100 上一段已經判斷過) >= 80 執行
    print("給你500")
elif score >= 60:
    print("給你100")
else:
    print("給我300")

# 4.
# 如果今天下雨 並且 你考 100 
#   我給你1000
# 否則
# 你給我100 

score = 90
rainy = True
# and 左右 True 才是 True
if rainy and score == 100:
    print("我給你1000")
else:
    print("你給我100")

# 5.
# 如果今天下雨 或者 你考 100 
#   我給你1000
# 否則
# 你給我100   
# or 兩者其一為 True 就是 True
rainy = False
score = 100
if rainy or score == 100:
    print("我給你1000")
else:
    print("你給我300")
# 6.
# 如果今天沒下雨 或者 你考 100 
#   我給你1000
# 否則
# 你給我100   
# not > boolean 判斷之後 變換判斷結果
score = 90
rainy = True
if not rainy or score == 100:
    print("我給你1000")
else:
    print("你給我300")
# 7.
# 如果今天沒下雨 或者 你沒有考 100 
#   我給你1000
# 否則
# 你給我100   

score = 90
rainy = True
if not (score == 100) or not(rainy):
    print("我給你1000")
else:
    print("你給我300")
# also
if score != 100 or not(rainy):
    print("我給你1000")
else:
    print("你給我300")
# also
if score != 100 or not rainy:
    print("我給你1000")
else:
    print("你給我300")
# also
if not (score == 100) or rainy == False:
    print("我給你1000")
else:
    print("你給我300")
# also
if not (score == 100) or rainy != True:
    print("我給你1000")
else:
    print("你給我300")

# 練習
def max_num(num1, num2, num3):
    if num1 >=  num2 and num2 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(2, 3, 5))

# 5