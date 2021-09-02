# 物件函式
class Phone:
    # __init__初始函式
    def __init__(self,os,number,is_waterproof):
        # 設定自己 self , 與需要的參數 os,number,is_waterproof
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
    # 類別內 物件函式定義時 可以繼續定義其他非初始的函式
    def is_ios(self): 
        # 傳入的第一參數 必須是 self
        # 這裡的self一樣是指本身
        if self.os == "ios": # 本身的os是否是 ios
            return True
        else:
            return False
    
    def add(self, number1, number2):
        return number1 + number2

phone1 = Phone("ios", 123, True)
# 定義 phone1 為 class 剛剛定義的 Phone
# phone1 呼叫 class 內定義的其他函式 is_ios() 與 add() 來使用
# class 使用本身的函示 加上點點來使用
print(phone1.is_ios())
print(phone1.add(5,6))