# class 類別 & object 物件
# 自己定義資料型態 來描述更多東西 物品
# 定義 Phone 這個類別的模板
class Phone:
    def __init__(self, os, number, is_waterproof):
        # __init__ 是物件名稱
        # os, number, is_waterproof 創建 class phone 時 需要的資訊
        # self 指的是我們創建的物件本身 object
        # 下面是我們的 self 物件的 屬性設定 os number is_waterproof
        self.os = os # self 的 os(line4) 使用我們傳入的 os
        self.number = number # self 的 os(line4) 使用我們傳入的 number
        self.is_waterproof = is_waterproof # self 的 os(line4) 使用我們傳入的 is_waterproof

# 建立第一隻 Phone
phone1 = Phone("ios",123,True) # 依照模板建立並給予模板所需資訊
print(phone1.number) # phone1.number 來取得 number 屬性

# 建立第二隻 Phone
phone2 = Phone("andriod", 456, False) # 依照模板建立並給予模板所需資訊
print(phone2.is_waterproof) # phone2.is_waterproof 來取得 is_waterproof 屬性