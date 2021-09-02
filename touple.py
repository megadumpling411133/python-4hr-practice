# touple 元組 
# 為了避免資料被修改 如經緯度 座標等等
scores = (90,80,60,70,50)
print(scores[0:2]) # 可用index取值 同list
print(len(scores)) # 可用len求長度 同list
# scores[0] = 30 # 元組不可變 
# print(scores)