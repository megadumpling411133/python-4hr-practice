# list 可存放許多資料型態
score1 = 90
score2 = 70
score3 = 60
score4 = 50
score5 = 80

# 更簡單的存入資料
scores = [90,70,60,50,80]
friends = ["Brent","Check","Abbie"]
things = [90,"Brent",True]
print("1",scores)
print("2",scores[-2])
print("3",scores[0:2])
print("4",scores[1:4])
print("5",scores[1:])
print("6",scores[-1])
phrase = "Hello Mr.White"
print(phrase[6:])
print(len(scores)) # 求長度
scores[0] = 30 # 修改
print(scores)
scores.extend(friends) # list 加在後面
print(scores)
scores.append(30) # list最後加30
print(scores)
scores.insert(2,30) # 在 index 2 插入 30
print(scores)
scores.remove(90) # 刪除特定數字
print(scores)
scores.pop # 清除最後值
print(scores)
scores.sorted() # 小到大排列
print(scores)
scores.revert() # 反轉排列
print(scores)
print(scores.index(30)) # 找到第一個出現的值並回傳位置index 

print(scores.count("Brent")) # 計算特定值出現次數
scores.clear # 清除list
print(scores)