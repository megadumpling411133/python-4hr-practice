# 函式 
# 預先寫好的程式碼 等待被呼叫執行
# 先定義 後呼叫
# 命名與變數規則相同
# tab 縮排

# 定義函式 尚未呼叫
def hello():
    print("hello")

# 呼叫函式!!
hello()

def hello(name,age):
    print("hello" + name + "你今年" + str(age) + "歲")

hello("David",31)


def add1(num1,num2):
    print(num1+num2)

add1(2,3)

# return 回傳概念
def add2(num1,num2):
    print(num1+num2)
    #return 10

# return 10 覆蓋了原先的呼叫 add(2,3) 的值 > 5 > 10
add2(2,3)

# return 的原因
# 函式不是執行完就結束 還要後續運算與處理
def add3(num1,num2):
    return num1+num2

print(add3(2,3))

# 下面執行結果為何?
def add4(num1,num2):
    print(num1+num2)
    return 10

value = add4(3,4)
print(value)
# 執行後 
# 1.函式定義
# 2.呼叫 add(3,4) 傳入 3,4 
# 3.執行函式 先印出 num1+num2 > 結果印出 7
# 4.再 return 10 被10取代 add(3,4) > 10
# value = 10
# print(value) > 結果印出 10
# 7
# 10

# 下面執行結果為何?
def add5(num1,num2):
    print(num1+num2)

value = add5(3,4)
print(value)

# python 沒有指定 return 預設 return None
# 7
# None

def add6(num1,num2):
    print(num1+num2)
    return 10
    print("hello")

value = add5(3,4)
print(value)

# 在函式定義時 定義在return之後的程式碼不被執行
# 就是呼叫只執行到return 不執行 print("hello")
# 7
# 10