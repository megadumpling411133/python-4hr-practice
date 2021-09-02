# 2D list & nested loop

nums = [0,1,2,3,4]
nums1 = [[0,1,2], [3,4,5], [6,7,8], [9]] # list 內的資料再放入 list > 兩層就是 2D

# 陣列的感覺更好看出 2D
nums1 = [
    [0,1,2], 
    [3,4,5], 
    [6,7,8], 
    [9]
]

# 取值
print(nums1[0][0]) # [行 row][列 colunm]
# 0
print(nums1[3][0])
# 9
print(nums1[2][2])
# 8
print("----------------------------------------")
# [行 row][列 colunm]
# for 的同時 建立 變數
# 2d list nested 先取第一層資料 就是 [0,1,2], [3,4,5], [6,7,8], [9] 四個 list
# 再取第二層資料 四個 list 每進入一個開始取 資料 e.g 進入 [0,1,2] 開始取出 0 > 1 > 2
for row in nums1: # for 的同時 建立 變數 row > 一圈取出 1 row
    for col in row: # for 的同時 建立 變數 col > 每圈取出 1 row 後 往內層 一圈取出 1 col
        print(col)
print("----------------------------------------")
# [行 row][列 colunm]
# for 的同時 建立 變數 
for a in nums1: # for 的同時 建立 變數 a > 一圈取出 1 row
    for b in a: # for 的同時 建立 變數 b > 每圈取出 1 row 後 往內層 一圈取出 1 col
        print(b)