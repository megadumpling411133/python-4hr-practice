# 檔案讀取 寫入
# 開檔案
# open("檔案路徑", mode="開啟模式", encoding="utf-8")
# encoding="utf-8" 支援中文
# 絕對路徑 檔案右鍵 內容 位置:就是絕對路徑 + 檔案名稱 > 使用斜線 (左手斜線) /
# e.g D:/lin ching shou/Desktop/Python_grandma_can_do/python/我的貼圖.jpg
# open("D:/lin ching shou/Desktop/Python_grandma_can_do/python/我的貼圖.jpg", mode="r") 

# 相對路徑 以程式位置做延伸 python 直接填入檔名 會視為 程式位置所在地加上檔名為 路徑
# e.g "我的貼圖.jpg"
# e.g open("我的貼圖.jpg", mode="r") 等價下方
# e.g open("D:/lin ching shou/Desktop/Python_grandma_can_do/python我的貼圖.jpg", mode="r") 等價上方

# mode="r" 讀取
# mode="a" 原檔案後寫東西
# mode="w" 副寫 > 新寫的蓋過


# file = open("D:/lin ching shou/Desktop/Python_grandma_can_do/python/123.txt", mode="r")
# print(file.read()) # 讀取檔案

# print(file.readline()) # 讀取一行
# print(file.readline()) # 讀取第二行

# 迴圈讀取所有行數
# for line in file:
#     print(line)

# print(file.readlines()) # 讀取複數行

# file = open("D:/lin ching shou/Desktop/Python_grandma_can_do/python/123.txt", mode="w") 
# mode="w" 覆寫
# print(file.write("hello")) # 寫入

# file = open("D:/lin ching shou/Desktop/Python_grandma_can_do/python/123.txt", mode="a", encoding="utf-8")
# file.write("\n你好")


# file.close() # 關閉來保留運算資源


with open("D:/lin ching shou/Desktop/Python_grandma_can_do/python/123.txt",mode="a", encoding="utf-8") as file: # 相當於 line 35
    file.write("\n哈哈") # 省去 close() 自動關閉